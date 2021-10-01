#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=karnold20/udacity-capstone

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker login -u $1 -p $2
docker tag udacity-capstone:latest karnold20/udacity-capstone:$3
# Step 3:
# Push image to a docker repository
docker push karnold20/udacity-capstone:$3