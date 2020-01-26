from model import Base, outfits

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_outfit(home, outfit):
	outfit_object = outfit()
	session.add(outfit_object)
	session.commit()