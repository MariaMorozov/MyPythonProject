FROM python:3
USER root
LABEL maintainer="maria.morozov@gmail.com"
RUN mkdir /docker_api
EXPOSE 5000
RUN chmod -R 755 /docker_api
COPY * /docker_api/
RUN pip install -r /docker_api/requirements.txt
#RUN pip install requests
#RUN pip install geopy

#COPY configurations.json /docker_api/
#COPY requirements.txt /docker_api/

WORKDIR "/docker_api"
#ADD api.py /
#CMD [ "python3", "./api.py" ]
ENTRYPOINT [ "/usr/local/bin/python3", "/docker_api/main.py" ]
#ENV FLASK_APP=int.py
#ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]