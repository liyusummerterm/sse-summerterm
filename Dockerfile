FROM python:3.7-alpine
ENV FLASK_CONFIG production
RUN apk add --update alpine-sdk && \
    mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt && \
    pip3 install gunicorn eventlet
CMD ["gunicorn","-b","0.0.0.0:80","-w","1","--worker-class","eventlet","backend:create_app()"]