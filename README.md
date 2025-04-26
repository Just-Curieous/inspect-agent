## Docker and Installation 
```bash
cd inspect-ai
docker build --platform=linux/amd64 -t pb-env -f Dockerfile.base .
docker run -it --name my-pb-env -v $(pwd):/workspace pb-env
docker exec -it my-pb-env bash
conda activate agent
```

## Setup experiment
Copy `env.sh.example` to `env.sh`. 
And configure:
- Your model and API key.
- Directory to your code and paper/questions

Remember to 
- Put `instructions.txt` under `$WORKSPACE_BASE`.
- Put your code repo under `$CODE_DIR`.

- To support Umich Azure API
```bash
cp /workspace/openai-3-78.py  /opt/conda/envs/agent/lib/python3.12/site-packages/inspect_ai/model/_providers/openai.py

```

## Start the agent

```
cd /workspace
bash start.sh
```



