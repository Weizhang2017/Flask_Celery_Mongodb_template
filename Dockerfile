FROM python:3.6.3
COPY Flask_Celery_Mongodb_template /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 80
ENV FLASK_APP=run.py
CMD flask run --host=0.0.0.0 --port=80
