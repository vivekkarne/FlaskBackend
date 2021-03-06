# Flaschemy Local Tester
  
#### Download Postgres:  
sudo apt-get install postgresql postgresql-contrib  
sudo service postgres@x.x status  
sudo service postgres@x.x start, if not running  
Ref: https://www.postgresqltutorial.com/install-postgresql-linux/  
  
#### Setup Database:  
  
Create a mock db in local system:  
sudo -u postgres createdb --owner={user} {dbname_test}  
ex: sudo -u postgres createdb --owner=student products_test  
  
  
login and see if the db is created:  
sudo -u postgres psql  
psql# \l  
  
#### Setup python env:  
  
Download python, preferably 3.6.13  
  
Navigate to src directory, activate venv using source env/bin/activate  
Or remove env folder and create your own venv using python3 -m venv env, activate env  
  
install requirements to run the flask server, pip3 install -r requirements.txt  
  
Environment is now set to run flask and postgres  
  
Verify the variables in .env file are set properly for testing:  
   - DATABASE_URL_TEST = "postgresql://student:student@localhost:5432/products_test"
   - DATABASE_URL = "postgresql://student:student@localhost:5432/products" -- Doesnt matter but for consistency
   
   - Check APP_SETTINGS is set to config.TestingConfig
   - APP_SETTINGS = "config.TestingConfig" -

Use flask-migrate to update tables in your database  
python3 manage.py db upgrade  
  
Seed data into the DB:  
python3 seeder.py seed_db   
  
Start the flask server  
python3 run.py run  
  
Open another terminal navigate to src, and activate virtual env  
Run the tester here using  
python3 tester.py  
