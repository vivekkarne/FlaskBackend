# API Description  
  
POST /review/{product_id}  
&nbsp;&nbsp;&nbsp;&nbsp;add a new review record, cannot update via POST, need to use put for updating a record  
  
PUT /review/{product_id}  
&nbsp;&nbsp;&nbsp;&nbsp;to insert new reviews or update if the review already exists  
  
GET /review/{product_id}  
&nbsp;&nbsp;&nbsp;&nbsp;Gets all of the reviews for a product, returns as an array of json's  
  
DELETE /review/{product_id}  
&nbsp;&nbsp;&nbsp;&nbsp;Deletes a review for the given product_id , user_id pair if it exists, sends appropriate error message with status otherwise  
  
GET /product/{product_id}  
&nbsp;&nbsp;&nbsp;&nbsp;Gets all the fields for a given product_id  
  
GET  /user/{user_id}  
&nbsp;&nbsp;&nbsp;&nbsp;Gets all the fields for a given user_id  
  
   
Reference: https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html