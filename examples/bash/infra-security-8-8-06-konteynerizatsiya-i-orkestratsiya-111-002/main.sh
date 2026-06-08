# Образы
docker build -t myapp:1.0 .
docker pull nginx:latest
docker push myregistry/myapp:1.0
docker images
docker rmi myapp:1.0
docker tag myapp:1.0 myregistry/myapp:1.0
docker save -o myapp.tar myapp:1.0
docker load -i myapp.tar

# Контейнеры
docker run -d -p 8080:80 --name web nginx
docker start web
docker stop web
docker restart web
docker kill web
docker ps -a
docker logs -f web
docker exec -it web sh
docker rm web

# Сети
docker network create mynet
docker network connect mynet web
docker network ls
docker network inspect mynet

# Тома
docker volume create myvol
docker volume ls
docker volume inspect myvol
docker volume rm myvol

# Система
docker info
docker version
docker system df
docker system prune
