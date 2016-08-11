FROM python:3.5-alpine
ADD . /server
ARG port
ARG username=admin
ARG password=password
ARG email=email@localhost
ENV port ${port}
EXPOSE $port
WORKDIR /server
RUN chmod 777 setup.sh && ./setup.sh
ENTRYPOINT python manage.py runserver 0.0.0.0:${port}
