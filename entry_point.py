#!/usr/bin/env python3
import argparse
import subprocess
import os
import sys
import shlex
import time

def run_docker_command(json_path, code_repo_path, inspect_path=None):
    """
    Run the start.sh script inside a Docker container with the provided paths.
    
    Args:
        json_path (str): Path to the JSON file
        code_repo_path (str): Path to the code repository
    """
    # Validate that the paths exist
    if not os.path.exists(json_path):
        print(f"Error: JSON file '{json_path}' does not exist.")
        sys.exit(1)
    
    if not os.path.exists(code_repo_path):
        print(f"Error: Code repository '{code_repo_path}' does not exist.")
        sys.exit(1)
    
    # Get current working directory
    current_dir = os.path.abspath(inspect_path)
    code_repo_path = os.path.abspath(code_repo_path)
    json_path = os.path.abspath(json_path)

    # Construct the Docker run command
    docker_id = str(int(time.time()))
    docker_command = [
        "docker", "run",
        "-it",
        "--name", f"pb-env-{docker_id}",
        "-v", f"{current_dir}:/workspace",
        "-v", "/:/all",
        "pb-env",
        "/bin/bash", "-c",
        f"cd /workspace && bash start.sh /all{code_repo_path} /all{json_path}"
    ]
    
    # Print the command that will be executed
    print(f"👩‍💻 Executing command: {' '.join(docker_command)}")
    
    try:
        # Run the Docker command
        result = subprocess.run(docker_command, check=True)
        print("Docker command executed successfully.")
        # return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error executing Docker command: {e}")
        return e.returncode
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

    try:
        subprocess.run(["docker", "rm", "-f", f"pb-env-{docker_id}"], check=True)
        print("Container removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing container: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run start.sh script inside Docker container with specified paths.")
    parser.add_argument("--json_path", required=True, help="Path to the JSON file")
    parser.add_argument("--code_repo_path", help="Path to the code repository")
    parser.add_argument("--inspect_path", required=True, help="Path to the inspect file")
    parser.add_argument("--remove-container", action="store_true", help="Remove the container after execution")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the Docker command
    return_code = run_docker_command(args.json_path, args.code_repo_path, args.inspect_path)
    
    sys.exit(return_code)

if __name__ == "__main__":
    main()

# python entry_point.py --json_path /home/ubuntu/Benchmark-Construction/logs/neurips2024/95262.json --code_repo_path /home/ubuntu/Benchmark-Construction/logs/neurips2024/MoE-Jetpack --inspect_path /home/ubuntu/inspect-agent