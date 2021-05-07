# ### models.py ###

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Date

# Base = declarative_base()

# def hi():
#    print("H1!")

# class Client(Base):
#     __tablename__ = 'client'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     author = Column(String)
#     pages = Column(Integer)
#     published = Column(Date)

#     def __repr__(self):
#         return "<Book(title='{}', author='{}', pages={}, published={})>"\
#                 .format(self.title, self.author, self.pages, self.published)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reviews(db.Model):
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


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    users = db.relationship("Reviews", back_populates = "product")

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
    products = db.relationship("Reviews", back_populates = "user")    

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
