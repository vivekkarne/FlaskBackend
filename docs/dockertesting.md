#Flaschemy Docker Tester

Testing in docker:

Stop local flask server if running
kill -9 pid

Stop local postgresql service if running
sudo service postgresql@xx stop

Clear volumes and stop the containers(assuming dockersetup.md is running), data is lost from the products db(ie. the main db)
docker-compose down -v

Change change products to products_test for POSTGRES_DB in docker_compose.yml

In .env file change APP_SETTINGS = "config.TestingConfig"

DATABASE URLs should have docker user whenever using docker and the database set to products_test, and the database host set to db of docker
   user = docker, password = docker, db_name = products_test (for DATABASE_URL_TEST), host=db

Go to base directory containing docker-compose.yml and run the command to spin up docker containers with updated configs:
   docker-compose up -d --build

Create and seed mock db for testing
   docker-compose exec app python manage.py db upgrade -- Create tables
   docker-compose exec app python seeder.py seed_db -- Seed data

Now run the tester.py to see all the outputs
   docker-compose exec app python tester.py

Post Completion for returning to default config:

Change the params back to point to original products db
   POSTGRES_DB=products -> in docker-compose.yml
   APP_SETTINGS = "config.ProductionConfig" in .env

Remove the volume for mock db
   docker-compose down -v

