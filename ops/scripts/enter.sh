#!/bin/bash

COMPONENT=treetop
CONTAINERS=$(docker ps --no-trunc -f "name=${COMPONENT}" --format "{{.Names}}"| \
sed "s/^${COMPONENT}_//" | sed "s/_1$//" | tr '\n' ' ')

printf "
  Write the name of the service that you want to access, possible choices are:
  ${CONTAINERS}
  Service name: " && read -r SERVICE

docker exec -ti ${COMPONENT}_${SERVICE} /bin/bash; history -c; history -r;
