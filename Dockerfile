FROM nginx
RUN mkdir /app
COPY frontend/dist /app
COPY nginx.conf /etc/nginx/nginx.conf