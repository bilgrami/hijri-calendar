docker build --rm -f "Dockerfile" -t bilgrami/hijri-calendar:latest .
docker run --rm -it -p 5000:5000/tcp bilgrami/hijri-calendar:latest