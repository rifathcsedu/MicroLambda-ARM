#!/bin/sh

echo "Building docker-func:latest-armhf ..."
docker build -t docker-func:latest-armhf . -f Dockerfile.armhf
