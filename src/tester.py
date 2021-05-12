from app import app
from models import db, User, Product, Review
import requests
import random, string
import json

def postReview(product_id, user_id, review, rating):
   url = f"http://localhost:5000/review/{product_id}"

   payload={'userid': user_id,
   'review': review,
   'rating': rating
   }
   files=[

   ]
   headers = {}

   response = requests.request("POST", url, headers=headers, data=payload, files=files)
   return response.text

def putReview(product_id, user_id, review, rating):
   url = f"http://localhost:5000/review/{product_id}"

   payload={'userid': user_id,
   'review': review,
   'rating': rating
   }
   files=[

   ]
   headers = {}

   response = requests.request("PUT", url, headers=headers, data=payload, files=files)
   return response.text

def getProductReviews(product_id):
   url = f"http://localhost:5000/review/{product_id}"

   payload={}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)
   return response.text

def getProductDetails(product_id):
   url = f"http://localhost:5000/product/{product_id}"

   payload={}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   return response.text

def getUserId(user_id):
   url = f"http://localhost:5000/user/{user_id}"

   payload={}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   return response.text

def deleteReview(product_id, user_id):
   url = f"http://localhost:5000/review/{product_id}"

   payload={'userid': user_id}
   files=[

   ]
   headers = {}

   response = requests.request("DELETE", url, headers=headers, data=payload, files=files)

   return response.text


def test_post_review():
   print("------Testing post review method---------")
   # Post a review and it should be accepted if it is the first time that user is reviewing a product
   print("Post review for the first time for a product user pair ", end = ": ")
   response_json = json.loads(postReview(1,2,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   if response_json["status"] == 200 and response_json["message"] == "Review added":
      print("Test Passed")
   else:
      print("Test Failed")
   
   deleteReview(1,2)

   # Post a review by the same user for the same product twice, should prompt th user to use PUT
   print("Post review should not accept duplicate inserts, prompts to use put for updation ", end = ": ")
   json.loads(postReview(1,2,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   response_json = json.loads(postReview(1,2,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   if response_json["status"] == 400 and response_json["message"] == "Malformed Query: use PUT /review/product_id to update an existing review":
      print("Test Passed")
   else:
      print("Test Failed")
   deleteReview(1,2)

def test_put_review():
   print("------Testing put review method---------")
   # Put a review and it should be accpeted if it is an insert, first time the user is reviewing the product
   print("Put review for the first time for a product user pair ", end = ": ")
   response_json = json.loads(putReview(3,2,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   if response_json["status"] == 200 and response_json["message"] == "Review added":
      print("Test Passed")
   else:
      print("Test Failed")
   
   deleteReview(3,2)

   # Post a review by the same user for the same product twice, should prompt th user to use PUT
   print("Put duplicate reviews, latest review updates the preceeding review ", end = ": ")
   json.loads(putReview(6,4,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   response_json = json.loads(putReview(6,4,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   if response_json["status"] == 200 and response_json["message"] == "Review updated":
      print("Test Passed")
   else:
      print("Test Failed")
   deleteReview(6,4)

def test_delete_review():
   print("------Testing delete review method---------")
   # Delete an existing review 
   print("Delete an existing review for a product by user ", end = ": ")
   json.loads(putReview(7,3,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ))
   response_json = json.loads(deleteReview(7,3))
   if response_json["status"] == 200 and response_json["message"] == "User review removed":
      print("Test Passed")
   else:
      print("Test failed")
   # Delete a non existing review
   print("Delete an non existing review for a product by user ", end = ": ")
   response_json = json.loads(deleteReview(7,3))
   if response_json["status"] == 400 and response_json["message"] == "Malformed query: Review does not exist for the following product_id, user_id pair":
      print("Test Passed")
   else:
      print("Test failed")

def test_get_reviews():
   print("------Testing get reviews method---------")
   # Put multiple reviews for a product, track size and see if all reviews are inserted
   print("Get multiple reviews ", end = ": ")
   putReview(8,5,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 )
   putReview(8,4,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 )
   putReview(8,3,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 )
   putReview(8,2,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 )
   putReview(8,1,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)), round(random.random(), 2)*10 ) #size=5
   if len(json.loads(getProductReviews(8))) == 5:
      print("Test Passed")
   else:
      print("Test Failed")

   deleteReview(8,1)
   deleteReview(8,2)
   deleteReview(8,3)
   deleteReview(8,4)
   deleteReview(8,5)
   
   # Test for product not having any reviews
   print("Product with no reviews ", end = ": ")
   if len(json.loads(getProductReviews(8))) == 0:
      print("Test Passed")
   else:
      print("Test Failed")


if __name__ == "__main__":
   print("------------Testing API methods------------")
   print()
   test_post_review()
   print()
   test_put_review()
   print()
   test_delete_review()
   print()
   test_get_reviews()