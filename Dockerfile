FROM python:3.8

LABEL maintainer="maria.morozov@gmail.com"

COPY requirements.txt /

RUN pip install -r /requirements.txt

ADD api.py /

CMD [ "python3", "./api.py" ]