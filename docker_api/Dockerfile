FROM python:3
USER root
LABEL maintainer="maria.morozov@gmail.com"
RUN mkdir /docker_api

RUN chmod -R 755 /docker_api

RUN pip3 install -r /docker_api/requirements.txt

WORKDIR "/docker_api"
COPY * /docker_api/
EXPOSE 5000
#ADD api.py /
#CMD [ "python3", "./api.py" ]  # CMD flask run --host=0.0.0.0
#ENTRYPOINT [ "/usr/local/bin/python3", "/docker_api/main.py" ]
ENV FLASK_APP=int.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]