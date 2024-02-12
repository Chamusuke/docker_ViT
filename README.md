# Vision Tranformer on Docker 
You can use huggingfase'transformers

Base image nvidia/cuda11.8 ubuntu22.04
- NVIDIA GPU
- python == 3.10
- pytorch cuda11.8
- transfomers (Hugging base)

## build
`docker build . -t vit_tut` \

## Dir
```
docker_vit/
├── Dockerfile
├── LICENSE
├── README.md
├── container_in.sh
├── data
│   ├── bird_dataset
│   │   ├── EfficientNetB0-525-(224 X 224)- 98.97.h5
│   │   ├── archive.zip
│   │   ├── birds.csv
│   │   ├── test
│   │   ├── train
│   │   └── valid
│   └── test_data
│       ├── Pembroke_Welsh_Corgi.jpg
│       ├── kiji.jpg
│       └── kingfisher.jpg
├── docker-compose.yml
├── run.sh
└── src
    ├── Fine_tune_ViT.ipynb
    ├── Make_Dataset.py
    ├── ViT_tut.ipynb
    ├── viT_Estimete_Fine_Tune.ipynb
    └── vit-weight
        ├── checkpoint-15500
        ├── checkpoint-16000
        ├── checkpoint-16500
        └── runs
```

## Usage
Please follow your host environment \
such as `-m & --cpus`
[メモリ、CPU、GPU に対する実行時オプション](https://docs.docker.jp/config/container/resource_constraints.html)
[Runtime options with Memory, CPUs, and GPUs](https://docs.docker.com/config/containers/resource_constraints/)
```
docker run -it --rm --name vit_docker \
  --volume=$PWD:/workspace:rw \
  --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
  -p 8888:8888 \
  -m 20g --cpus="8.0" \
  --gpus=all \
  vit_tut:latest \
  /bin/sh -c "jupyter-lab --no-browser --port=8888 --ip=0.0.0.0 \
    --allow-root --NotebookApp.token=''"
```

