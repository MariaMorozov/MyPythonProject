FROM python:3
USER root
LABEL maintainer="maria.morozov@gmail.com"
RUN mkdir /docker_api
RUN chmod -R 755 /docker_api
#RUN pip install -r /requirements.txt
RUN pip install requests
RUN pip install geopy
COPY *.py /docker_api/
COPY configurations.json /docker_api/
#COPY requirements.txt /docker_api/
#RUN chmod -R 755 /docker_api
WORKDIR "/docker_api"
#ADD api.py /
#CMD [ "python3", "./api.py" ]
ENTRYPOINT [ "/usr/local/bin/python3", "/docker_api/main.py" ]