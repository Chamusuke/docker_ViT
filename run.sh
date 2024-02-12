docker run -it --rm --name vit_docker \
  --volume=$PWD:/workspace:rw \
  --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
  -p 8888:8888 \
  -m 20g --cpus="8.0" \
  --gpus=all \
  vit_tut:latest \
  /bin/sh -c "jupyter-lab --no-browser --port=8888 --ip=0.0.0.0 \
    --allow-root --NotebookApp.token=''"
