#!/usr/bin/env bash
set -o errexit

# Set the image name
IMAGE_NAME="phx2600/thebutton"

# Set script directory path
SCRIPT_DIR="$(dirname $(readlink -f ${0}))"

# Set image tag
TAG="local"

# Build the image
docker build --force-rm --pull --tag ${IMAGE_NAME}:${TAG} ${SCRIPT_DIR}

# Notify user of success
echo "Sucessfully created image: ${IMAGE_NAME}:${TAG}"
