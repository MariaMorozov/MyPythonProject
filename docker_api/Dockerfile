FROM python:3
USER root
LABEL maintainer="maria.morozov@gmail.com"
RUN mkdir /myproject1
RUN chmod -R 755 /myproject1
RUN pip install -r /requirements.txt
COPY *.py /myproject1/
COPY configurations.json /myproject1/
COPY requirements.txt /myproject1/
WORKDIR "/myproject1"
#ADD api.py /
#CMD [ "python3", "./api.py" ]
ENTRYPOINT [ "/usr/local/bin/python3", "/myproject1/main.py" ]