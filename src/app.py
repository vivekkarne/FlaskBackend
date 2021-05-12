import os
from flask import Flask, request,render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, User, Review

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

import json


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

# Actual APIs

@app.route('/product/<product_id>', methods = ['GET'])
def get_product(product_id):
   if request.method == 'GET':
      product = db.session.query(Product).get(product_id)
      if product is not None:
         return jsonify(product.as_dict())
      return jsonify(error="Product Not found")

@app.route('/user/<user_id>', methods = ['GET'])
def get_user(user_id):
   if request.method == 'GET':
      user = db.session.query(User).get(user_id)
      if user is not None:
         return jsonify(user.as_dict())
      return jsonify(error="User Not found")

@app.route('/review/<product_id>', methods = ['POST','PUT','GET','DELETE'])
def review_operations(product_id):
   if request.method == 'POST':
      product = db.session.query(Product).get(product_id)

      if product is not None:
         user_id = request.form['userid']
         review = request.form['review']
         rating = request.form['rating']

         # review_obj = Review(review=review, rating=rating)
         user = db.session.query(User).get(user_id)

         if user is None:
            return jsonify({"status": 400, "message": "Malformed query: User does not exits"})
         
         if any(user.id == review_user.user_id for review_user in product.users):
            return jsonify({"status": 400, "message": "Malformed Query: use PUT /review/product_id to update an existing review"})

         review_obj = Review(review=review, rating=rating)
         review_obj.user = user
         product.users.append(review_obj)
         db.session.commit()

         # try:
         #    db.session.commit()
         # except IntegrityError as e:
         #    assert isinstance(e.orig, UniqueViolation)
         #    return jsonify({"status": 400, "message": "Malformed Query: use PUT /review/product_id to update an existing review"})
         
         return jsonify({"status": 200, "message": "Review added"})

      return jsonify({"status": 400, "message": "Malformed query: Product does not exits"})

   if request.method == 'PUT':
      product = db.session.query(Product).get(product_id)

      if product is not None:
         user_id = request.form['userid']
         review = request.form['review']
         rating = request.form['rating']

         user = db.session.query(User).get(user_id)

         if user is None:
            return jsonify({"status": 400, "message": "Malformed query: User does not exits"})

         if any(user.id == review_user.user_id for review_user in product.users):
            update_assoc = Review.query.filter_by(user_id=user.id, product_id=product_id).first()
            update_assoc.review = review
            update_assoc.rating = rating
            db.session.commit()
            return jsonify({"status": 200, "message": "Review updated"})

         review_obj = Review(review=review, rating=rating)
         review_obj.user = user
         product.users.append(review_obj)
         db.session.commit()

         # try:
         #    db.session.commit()
         # except IntegrityError as e:
         #    assert isinstance(e.orig, UniqueViolation)
         #    return jsonify({"status": 400, "message": "Malformed Query: use PUT /review/product_id to update an existing review"})
         
         return jsonify({"status": 200, "message": "Review added"})

      return jsonify({"status": 400, "message": "Malformed query: Product does not exits"})

   if request.method == 'GET':
      product = db.session.query(Product).get(product_id)

      if product is not None:
         all_reviews = Review.query.filter_by(product_id=product_id).all()
         for review in all_reviews:
            print(review.as_dict())
         return json.dumps([review.as_dict() for review in all_reviews])

      return jsonify({"status": 400, "message": "Malformed query: Product does not exits"})
   
   if request.method == 'DELETE':
      product = db.session.query(Product).get(product_id)

      if product is not None:
         user_id = request.form['userid']
         user = db.session.query(User).get(user_id)

         if user is None:
            return jsonify({"status": 400, "message": "Malformed query: User does not exits"})

         if any(user.id == review_user.user_id for review_user in product.users):
            Review.query.filter_by(user_id=user.id, product_id=product_id).delete()
            db.session.commit()
            return jsonify({"status": 200, "message": "User review removed"})
         
         return jsonify({"status": 400, "message": "Malformed query: Review does not exist for the following product_id, user_id pair"})

      return jsonify({"status": 400, "message": "Malformed query: Product does not exits"})


if __name__ == '__main__':
   app.run()