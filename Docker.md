Install docker engine
Install docker-compose
docker-compose build
docker-compose up -d --build // rebuild if necessary
docker ps
docker-compose exec app python seeder.py create_db
docker volume ls
docker volume inspect