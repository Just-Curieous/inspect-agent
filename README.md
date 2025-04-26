## Docker and Installation 
```bash

docker build -t pb-env .
docker run -it --name my-pb-env -v $(pwd):/workspace pb-env
docker exec -it my-pb-env bash
```

```bash

conda activate agent    

pip install inspect_ai==0.3.78

pip install openai 
pip install tiktoken
```



