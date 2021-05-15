# base image  
FROM python:3.7   
# setup environment variable  
ENV DockerHOME=/code
# set work directory  
RUN mkdir -p $DockerHOME  
# where your code lives  
WORKDIR $DockerHOME  
EXPOSE 8000
# copy whole project to your docker home directory
COPY . $DockerHOME  

RUN pip install -r requirements.txt  
