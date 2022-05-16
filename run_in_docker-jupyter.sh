docker build --rm -t bpu -f Dockerfile .
docker run --rm -i -p 8888:8888 -v "$PWD":/home/jovyan/work bpu
