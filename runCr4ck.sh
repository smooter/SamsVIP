#!/usr/bin/env bash
PROJECT="samsvip"
COMPOSE_FILE="./compose/samsvip.yml"

docker-compose -p $PROJECT -f $COMPOSE_FILE build
docker-compose -p $PROJECT -f $COMPOSE_FILE rm -f
docker-compose -p $PROJECT -f $COMPOSE_FILE up -d
