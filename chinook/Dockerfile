FROM python:3.5-alpine
ADD . /server
ARG app_port
ARG db_name
ARG db_user
ARG db_password
ARG db_port
ENV app_port=${app_port}
ENV DOCKERIZE_VERSION=v0.2.0
EXPOSE $app_port
WORKDIR /server
RUN    apk update \
    && apk add gcc postgresql-dev musl-dev openssl \
    && pip install -r requirements.txt
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz
ENTRYPOINT dockerize -wait tcp://db:$db_port && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:${app_port}
