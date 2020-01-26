from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Outfit(Base):
	__tablename__ = 'outfits'
	id = Column(Integer, Primery_key=True)
	image = Column(String)
	description = Column(String) 