# Vision Tranformer on Docker 
You can use huggingfase'transformers

Base image nvidia/cuda11.8 ubuntu22.04
- NVIDIA GPU
- python == 3.10
- pytorch cuda11.8
- transfomers (Hugging base)

# Usage
Please follow your host environment \
docker-compose.yml \
```
...
    limits:
      cpus: "6"
      memory: 16g
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
      memory: 16g
      cpus: "6"
mem_swappiness: 0
memswap_limit: 16g #swap = memswap_limit - memory
...
```

```
docker compose up -d  && docker exec -it --user user ViT bash
```
In container, Running jupyterlab 
You can develop in browser
```
jupyter-lab --ip 0.0.0.0
```


