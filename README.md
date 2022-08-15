# coursework_5

docker run --rm --publish 127.0.0.1:5432:5432 --env POSTGRES_USER=skymarket --env POSTGRES_PASSWORD=skymarket --name skymarket --detach postgres:14.4-alpine