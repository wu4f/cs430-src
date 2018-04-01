# Builds container from Dockerfile and requirements.txt
sudo docker build -t flask-hello-world:latest .

# List container image
sudo docker images

# Login to Docker Hub
sudo docker login

# Tag image to your Docker Hub repo
#    use -f if replacing
sudo docker tag flask-hello-world wuchangfeng/flask-hello-world

# Push image to your Docker Hub repo
sudo docker push wuchangfeng/flask-hello-world

# Run the image (equivalent to docker pull followed by docker start)
sudo docker run -d -p 8000:8000 wuchangfeng/flask-hello-world

# View active and stopped containers
sudo docker ps -a

# Stop the container
sudo docker stop <nameof_container>

# Start the container
sudo docker start <nameof_container>

# Remove the container
sudo docker rm <nameof_container>

# Remove the local container image (assuming its containers have been deleted)
sudo docker rmi wuchangfeng/flask-hello-world
