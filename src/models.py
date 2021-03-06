# ### models.py ###

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    review = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user = db.relationship("User", back_populates="products")
    product = db.relationship("Product", back_populates="users")

    __table_args__ = (
        db.UniqueConstraint(user_id, product_id),
    )

    # def __init__(self, review, rating):
    #     self.review = review
    #     self.rating = rating
    
    def __repr__(self):
        return f"{self.review} : {self.rating}"

    def as_dict(self):
        return dict(user_id = self.user_id, user_name = self.user.name, product_id = self.product_id, product_name = self.product.name, review= self.review, rating=self.rating)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    users = db.relationship("Review", back_populates = "product")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}:{self.description}"

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    products = db.relationship("Review", back_populates = "user")    

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
