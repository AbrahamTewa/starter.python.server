FROM python:3.5-slim
ADD . /server
WORKDIR /server
EXPOSE 8080
RUN    apk update
    && apk add gcc postgresql-dev musl-dev
    && pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
