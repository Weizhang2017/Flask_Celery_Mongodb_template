#### A simple template for using flask with celery and mongodb

> requirments

1. Rabbitmq(sudo rabbitmq-server)
2. Mongodb

Run with Dockerfile
docker build -t Flask_Celery_Mongodb_template:latest .
docker run -p 5000:80 Flask_Celery_Mongodb_template:latest
