# docker.io
Learning to build docker for any tech stack


# Docker Master Class: From Basics to Advanced with Docker Compose


1. Introduction to Docker


1.1. What is Docker?

    - Introduction to containerization

    -  Benefits of using Docker 1.2. Installing Docker

    - Installation steps for different operating systems (Windows, macOS, Linux) 1.3. Basic Docker Commands

    - `docker version`: Check installed Docker version

    - `docker info`: Display system-wide information

    - `docker run`: Run a container

    - `docker ps`: List running containers

    - `docker stop`: Stop a running container

2. Docker Images and Containers

2.1. Understanding Docker Images

    What is an image?

    Using Docker Hub 2.2. Creating and Managing Containers

    docker create: Create a container

    docker start: Start a stopped container

    docker rm: Remove a container

    docker rmi: Remove an image 2.3. Dockerfile

    Writing a basic Dockerfile

    Building an image with docker build

    Understanding layers in Dockerfile

3. Networking and Storage

3.1. Docker Networking

    Networking basics

    docker network ls: List networks

    docker network create: Create a network

    docker network connect: Connect a container to a network 3.2. Docker Volumes

    Understanding volumes

    docker volume create: Create a volume

    docker volume ls: List volumes

    docker run -v: Mounting volumes to containers