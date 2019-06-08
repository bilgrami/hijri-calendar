#!/usr/bin/env bash
docker build --rm -f "Dockerfile" -t bilgrami/hijricalendar:latest .
docker push bilgrami/hijricalendar:latest
# docker run --rm -it -p 5000:5000/tcp bilgrami/hijricalendar:latest
