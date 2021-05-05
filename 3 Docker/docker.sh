#!/bin/bash

mkdir test

cp docker.py test/.

echo "FROM python" >> test/Dockerfile

echo "RUN pip install flask" >> test/Dockerfile

echo "COPY  docker.py /home/myapp/" >> test/Dockerfile

echo "EXPOSE 8080" >> test/Dockerfile

echo "CMD python3 /home/myapp/docker.py" >> test/Dockerfile

cd test

docker build -t docker .

docker run -t -d -p 8080:8080 --name Piki docker

docker ps -a
