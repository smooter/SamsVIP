docker build -t samsvip:latest .
docker rm -f samscheck
docker run --name samscheck -d samsvip:latest
