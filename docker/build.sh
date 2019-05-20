#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage  : $0 <path_to_docker_file> <tag>"
    echo "Example: $0 ./docker/test-image hackorma/test:1.0"
    exit 1
fi

docker build \
   --compress \
   --file $1/Dockerfile \
   --force-rm \
   --no-cache \
   --rm \
   --tag $2 \
   $1
