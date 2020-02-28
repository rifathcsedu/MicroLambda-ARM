#!/bin/sh
which docker

if [ $? -eq 0 ]
then
    docker --version | grep "Docker version"
    if [ $? -eq 0 ]
    then
        echo "docker existing"
    else
        curl -sSL https://get.docker.com | sh
    fi
else
    curl -sSL https://get.docker.com | sh
fi
#etc.
sudo usermod pi -aG docker
