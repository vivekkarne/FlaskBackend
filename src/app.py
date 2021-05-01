import os
from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, User

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_product = Product(name=name, description=description)
        db.session.add(new_product)
        db.session.commit()
        return f"Done!!"

@app.route('/user/<user_name>', methods = ['PUT'])
def put_user(user_name):
   if request.method == 'PUT':
      new_user = User(name=user_name)
      db.session.add(new_user)
      db.session.commit()
      return f"User Added!"

if __name__ == '__main__':
   app.run()