Setup Database:

Create a db in local system:
sudo -u postgres createdb --owner={user} {dbname}
ex: sudo -u postgres createdb --owner=student products


login and see if the db is created: 
sudo -u postgres psql
psql# \l

Setup python env:

Download python, preferably 3.6.13

Navigate to src directory, activate venv using source env/bin/activate
Or remove env folder and create your own venv using python3 -m venv env, activate env

install requirements to run the flask server, pip3 install -r requirements.txt

Environment is now set to run flask and postgres

Verify the variables in .env file are set properly
   Check DATABASE_URL is set to the correct value as mentioned in the .env file
   Check APP_SETTINGS is set to config.ProductionConfig


Use flask-migrate to update tables in your database
python3 manage.py db upgrade

Seed data into the DB:
python3 seeder.py seed_db

Start the flask server
python3 run.py run

Now you must be able to access the rest end points as per the [API DOCUMENTATION](docs/apidocs.md) and observer the responses

Note: Use migrate and upgrade when schema is changed
python3 manage.py db migrate
python3 manage.py db upgrade


