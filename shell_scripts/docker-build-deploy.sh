#!/usr/bin/env bash

set -e;

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/.."

image_tag="latest";
image_full_name="bilgrami/hijricalendar:$image_tag";

echo "Building image '$image_full_name'";
docker build -f "Dockerfile" -t "$image_full_name" .;

echo "Authenticating";
echo "$DOCKER_PASS" | docker login -u="$DOCKER_USERNAME" --password-stdin;

echo "Pushing image '$image_full_name'";
docker push "$image_full_name";
echo "Push finished!";

exit 0;

# docker build --rm -f "Dockerfile" -t bilgrami/hijricalendar:latest .
# docker push bilgrami/hijricalendar:latest
# docker run --rm -it -p 5000:5000/tcp $image_full_name
# docker run -it --entrypoint bash -p 5000:5000/tcp bilgrami/hijricalendar:latest
