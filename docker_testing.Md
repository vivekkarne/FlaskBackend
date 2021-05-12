Testing in docker:

Stop local postgres server if already running, sudo service postgresql@x.x-main stop

Migrate old actual databases before clearing volumes, so that schema is up to date
"docker-compose exec app python manage.py db migrate",
if doesnt work do "docker-compose exec app python manage.py db stamp head" and then "docker-compose exec app python manage.py db migrate"
docker-compose exec app python manage.py db migrate

Clear volumes and down the containers, loses all data
docker-compose down -v

Change change products to products_test for POSTGRES_DB in docker_compose.yml

In .env file change APP_SETTINGS = "config.TestingConfig"

DATABASE URLs should have docker user whenever using docker and the database set to products_test, and the database host set to db of docker
   user = docker, password = docker, db_name = products_test (for DATABASE_URL_TEST), host=db

Go to base directory containing docker-compose.yml and run the command to spin up docker containers with updated configs:
   docker-compose up -d --build

Create and seed mock db for testing
   docker-compose exec app python seeder.py create_db -- Create tables
   docker-compose exec app python seeder.py seed_db -- Seed data

Now run the tester.py to see all the outputs

Change the params back to point to original products db
   POSTGRES_DB=products -> in docker-compose.yml
   APP_SETTINGS = "config.ProductionConfig" in .env

Remove the volume for mock db
   docker-compose down -v

Go to base directory containing docker-compose.yml and run the command to spin up docker containers with updated configs:
   docker-compose up -d --build

Apply previously backup migration
   docker-compose exec app manage.py db upgrade

Apply seed data:
   docker-compose exec app seeder.py seed_db

Database products is again in prod mode and ready to go
