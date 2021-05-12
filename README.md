# FlaskBackend

Install postgres in local
sudo apt-get install postgresql postgresql-contrib


sudo -u postgres createuser --superuser student
sudo -u student createdb products
psql -U student -d products
sudo -u postgres psql
CREATE USER name [ [ WITH ] option [ ... ] ] to create user


Create venv for flask
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

The src code contains the codebase for the flask server
app.py
   - Flask App
config.py
   - APP - DB configs

Add app_settings and database_url to path so to .env
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/products"



DB Schema
products Table:
id - integer not null primary key
name - text not null
description - text null

sudo update-alternatives --config python3


Migration:
python manage.py db init
python manage.py db migrate
python manage.py db upgrade