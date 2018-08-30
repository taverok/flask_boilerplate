# Flask Boilerplate

Flask boilerplate app

- docker based
- microservice oriented

### TODO:
- ansible deployment 
- tests
- docker entrypoint

## docker-compose
create docker-compose.yml file one level above of this app
```
version: '2'
services:
  web:
    build: ./sample_app
    ports:
      - "5000:5000"
    links:
      - db1:mysql
    container_name: sample_app_web
    depends_on:
      - db1
    stdin_open: true
    tty: true
    environment:
        PORT: 5000
        SECRET_KEY: 'you-will-never-guess'
        DEBUG: 1
        MYSQL_ROOT_PASSWORD: rootpass
        DB_USERNAME: sample_user
        DB_PASSWORD: sample_password
        DB_HOST: mysql
        DATABASE_NAME: sample
  db1:
    image: mysql:5.7
    restart: always
    container_name: sample_app_db_1
    ports:
      - "13306:3306"
    environment:
        MYSQL_USER: sample_user
        MYSQL_PASSWORD: sample_password
        MYSQL_ROOT_PASSWORD: rootpass
        MYSQL_DATABASE: sample

```

## Using Docker
- Run `docker-compose up`
- In a new terminal or tab run:
    - `docker exec -it sample_app_web flask db init` to initialize migrations
    - `docker exec -it sample_app_web flask db migrate` 
    - `docker exec -it sample_app_web flask db upgrade` to create tables
- Open `http://localhost:5000` in your browser

## Production
- Use Gunicorn `gunicorn wsgi:app --bind 0.0.0.0:$PORT --reload`
