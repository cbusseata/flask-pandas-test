DOCKER_COMPOSE_LOCATION := "ops/docker/docker-compose.yml"
COMPONENT               := treetop

all: down build up logs
no-cache: down build-no-cache up
up:
	docker-compose -f $(DOCKER_COMPOSE_LOCATION) up -d
down:
	docker-compose -f $(DOCKER_COMPOSE_LOCATION) down -v
build:
	docker-compose -f $(DOCKER_COMPOSE_LOCATION) build
build-no-cache:
	docker-compose -f $(DOCKER_COMPOSE_LOCATION) build --no-cache
enter:
	@./ops/scripts/enter.sh
logs:
	docker logs treetop_app -f

-include Makefile.d/*.mk
