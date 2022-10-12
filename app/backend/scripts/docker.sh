# commands notes, not to be run as a script
# pull this image
docker pull amazonlinux:2

# see all images
docker images | grep amazon

# run this image in a detached mode
# -p: map localhost:5000 -> this container:5000
docker container -dit -p 5000:5000 --name aml2 amazonlinux:2

# see running containers, get container ID or name
docker ps

# Copy our code into the home directory of the container
docker cp . aml2:/home

# exec this command and drop inside of the container
docker exec -it aml2 /bin/bash
docker attach aml2

# install python3.7 with the yum package manager
yum install python3.7 -y

cd scripts && bash scripts/setup.sh

flask run --host=0.0.0.0

# stop the container
docker stop aml2