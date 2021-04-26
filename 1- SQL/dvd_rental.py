
__author__ = "Patricio Henderson"
__email__ = "patricio.henderson.v@gmail.com"
__version__ = "1.1"

import sqlite3
import sqlalchemy
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Creating DB
engine = sqlalchemy.create_engine('sqlite:///dvd_rental.db')
base = declarative_base()
session = sessionmaker(bind=engine)()



class Autor(base):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class dvd(base):
    __tablename__ = "book" 
    id = Column(Integer,primary_key=True)
    title = Column(String)
    pags = Column(Integer)
    author_id = Column(Integer, ForeignKey('autor.id'))
    author = relationship('Autor')


def create_schema():
    base.metadata.drop_all(engine)

    base.metadata.create_all(engine)

if __name__ == "__main__":
    create_schema()
                