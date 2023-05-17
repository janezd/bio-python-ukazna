docker build --rm -t bpu -f Dockerfile-jupyter .
docker run --rm -i -p 8888:8888 -v "$PWD":/home/jovyan/work -w "/home/jovyan/work" bpu
