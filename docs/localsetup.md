# Flaschemy Local Runner

#### Download Postgres:  
sudo apt-get install postgresql postgresql-contrib  
sudo service postgres@x.x status  
sudo service postgres@x.x start, if not running  
Ref: https://www.postgresqltutorial.com/install-postgresql-linux/  

#### Setup Database:  

Create a db in local system:  
sudo -u postgres createdb --owner={user} {dbname}  
ex: sudo -u postgres createdb --owner=student products  
  
   
login and see if the db is created:   
sudo -u postgres psql  
psql# \l  
  
#### Setup python env:  
Download python, preferably 3.6.13  
Navigate to src directory, activate venv using source env/bin/activate  
Or remove env folder and create your own venv using python3 -m venv env, activate env  
  
install requirements to run the flask server, pip3 install -r requirements.txt  
  
Environment is now set to run flask and postgres  
  
Verify the variables in .env file are set properly  
   - Check DATABASE_URLs are set to the correct value as mentioned in the .env file  
   - DATABASE_URL = "postgresql://student:student@localhost:5432/products"  
   - DATABASE_URL_TEST = "postgresql://student:student@localhost:5432/products_test" -- Doesnt matter but for consistency  
   
   - Check APP_SETTINGS is set to config.ProductionConfig
   - APP_SETTINGS = "config.ProductionConfig" 
  
Use flask-migrate to update tables in your database  
python3 manage.py db upgrade  
  
Seed data into the DB:  
python3 seeder.py seed_db  
  
Start the flask server  
python3 run.py run  
  
Now you must be able to access the rest end points at http://localhost:5000/ and use the [API Documentation](./apidocs.md) to observe the responses  
  
Note: Use migrate and upgrade when schema is changed  
python3 manage.py db migrate  
python3 manage.py db upgrade  

