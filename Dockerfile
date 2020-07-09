FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt && \
    pip3 install waitress
CMD ["waitress-serve","--port","80","--call","backend:create_app"]