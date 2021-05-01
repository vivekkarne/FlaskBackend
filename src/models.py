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
 
class Product(db.Model):
    __tablename__ = 'products'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    description = db.Column(db.String())
 
    def __init__(self, name, description):
        self.name = name
        self.description = description
 
    def __repr__(self):
        return f"{self.name}:{self.description}"