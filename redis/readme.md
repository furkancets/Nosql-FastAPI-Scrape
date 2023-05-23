docker build  -t scrape-redis  -f Dockerfile .

docker run -it --rm -p 6379:6379 scrape-redis

echo PING | nc 127.0.0.1 6379 