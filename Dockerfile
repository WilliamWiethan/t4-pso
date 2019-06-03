FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

ADD requirements.pip .
RUN pip install -r requirements.pip

CMD sh script.sh
