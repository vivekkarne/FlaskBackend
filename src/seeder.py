from app import app
from models import db, User, Product
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

def seed_users():
   names = ["John", "Meredith", "Ismail", "Ram", "Aaron"]
   for i in range(len(names)):
      db.session.add(User(name=names[i]))
   db.session.commit()


def seed_products():
   products = ["Sheets", "Detergent", "Paper towels", "Coke", "Fan", "Bag", "Bulbs", "Batteries", "Deodrant", "Pillow"]
   descriptions = ["Stay warm", "Top load detergent, very strong", "Soft and powerful", "Refreshing carbonated drink", "Get a fan this summer",
   "water-proof bag", "Lights up your world", "Long lasting batteries", "24 hour freshness", "Soft and comfortable for a good nights sleep"]
   for i in range(len(products)):
      db.session.add(Product(name=products[i], description=descriptions[i]))
   db.session.commit()


@cli.command("create_db")
def create_db():
   db.drop_all()
   db.create_all()
   db.session.commit()

@cli.command("seed_db")
def seed_db():
   seed_users()
   seed_products()

if __name__ == "__main__":
   cli()