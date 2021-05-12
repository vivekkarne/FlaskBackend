#Flaschemy Docker Runner

Install Docker Engine
https://docs.docker.com/engine/install/
docker-compose --version

Install Docker Compose
https://docs.docker.com/compose/install/
docker --version

Stop local flask server if running
kill -9 pid

Stop local postgresql service if running
sudo service postgresql@xx stop

Go to base directory, where docker file is present

Clear any volumes if present(only when you have used the docker setup previously for testing and forgot the last step in dockertesting.md, otherwise cleaning will cause data loss)
docker volume ls
docker volume inspect xyz
docker volume rm xyz

Use the default configurations of the .env file:
DATABASE_URL_TEST = "postgresql://docker:docker@db:5432/products_test"
DATABASE_URL = "postgresql://docker:docer@db:5432/products"
APP_SETTINGS = "config.ProductionConfig"

And the docker-compose.yml file:
POSTGRES_DB=products

Run 
docker-compose up -d --build
or
docker-compose build
docker-compose up -d

Check that the processes are up
docker ps or docker-compose ps

Run flask-migrate upgrade to create tables in the products db
docker-compose exec app python manage.py db upgrade

Seed data into the database
docker-compose exec app python seeder.py seed_db

Now, the docker flask server should be accessible at http://localhost:5000, and also the docker db server should be accessibe at localhost:5432, if needed(pgAdmin client).

To down the containers and persist data use:
docker-compose down