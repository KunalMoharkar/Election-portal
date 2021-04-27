# base image  
FROM python:3.7   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  
# set work directory  
RUN mkdir -p $DockerHOME  
# where your code lives  
WORKDIR $DockerHOME  
# install dependencies  
RUN pip install --upgrade pip  
# copy whole project to your docker home directory
COPY . $DockerHOME  
# run this command to install all dependencies  
EXPOSE 8000

RUN pip install -r requirements.txt  
# start server  
CMD ["python", "Electionportal/manage.py", "runserver", "0.0.0.0:8000"]