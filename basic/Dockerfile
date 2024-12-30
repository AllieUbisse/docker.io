# A docker file contains instructions to buld an image and all commands are ussually all CAPS

# The <FROM> command is used to pull a base image os.
# FROM image-name:image-tag
FROM debian:latest

# The <WORKDIR> is the 1st directory the program will CD to it once it starts.
# All commands will start executing from this DIR.
WORKDIR /usr/src

# The <RUN> command will help execute linux based commnads.
# e.g <apt-get> a linux package manager to install required softwares.
RUN apt-get update && \
    apt-get install -y python3 python3-pip 

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Using <RUN> to execute linux command to create a non root user, to run the program with configurable permissions.
RUN useradd --create-home appuser
USER appuser

# The <COPY> command will copy files from the local machine over to the image.
COPY . /usr/src

# The <ENV> will help set environment variables from your secured location, use dockerignore to prevent testing key to be exposed.
ENV API_KEY='STORE-KEYS-SECURELY'

# The <EXPOSE> is a command that allows us to enable network ports  access our application by external traffic.
EXPOSE 8000

# The <CMD> will execute once the image is built to run the application inside the container.
# CMD ["python3","-m","http.server","8000"]

# The <ENTRYPOINT> allows you to pass arguments to the command when you run it (optional).
ENTRYPOINT ["python3","-m", "http.server" ]

CMD ["8000"]


HEALTHCHECK --interval=30s --timeout=10s\
   CMD curl -f http://localhost:6969/health || exit 1


# The <VOLUME> command will help mount to a persisting storage to access and store file suppose the 
VOLUME /db/data


# Add metadata by using the command  <LABEL>
LABEL maintainer="Troinux"
LABEL version="1.0.0"
LABEL description="Basic dockerFile to get-started"