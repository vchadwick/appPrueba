# appPrueba

## 0. Start Docker

Start Docker

## 1. Environment variables

Create .env file with:

````
# Database variables
POSTGRES_DB='apppruebadata'
POSTGRES_USER='postgres_user'
POSTGRES_PASSWORD='postgres_password'
POSTGRES_NAME='postgres'
# Keycloak variables
KEYCLOAK_ADMIN='admin'
KEYCLOAK_ADMIN_PASSWORD='admin'
KEYCLOAK_USER='admin'
KEYCLOAK_PASSWORD='admin'
````

## 2. Create images

Run the following command:
```
docker-compose build
```

## 3. Upload containers

Run the following command:
```
docker-compose up
```

## 4. Migrate database and create superuser (Django)

Run the following commands:
```
docker-compose run backend python3 manage.py migrate
docker-compose run backend python3 manage.py createsuperuser
```

## 4. Especifications

* http://localhost:8080 KeyCloak dashboard
* http://localhost:3000 Frontend
* http://localhost:3001 Backend

## 5. Useful links

* https://documenter.getpostman.com/view/7294517/SzmfZHnd
