### crud.py ###

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

from models import Base

print(os.getenv('DATABASE_URL'))
engine = create_engine(os.getenv('DATABASE_URL'))
Base.metadata.create_all(engine)