# install sqlite from sqlite.org
# pip install sqlalchemy
# pip install pysqlite
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = sqlalchemy.create_engine('sqlite:///new_db.db', echo=True)

Base = declarative_base() 

class Scrapes(Base):
    __tablename__ = 'sprapes'
  
  #Have an ID column because player attributes (name, etc) are not unique
    post_id = Column(Integer, primary_key=True)
    link = Column(String, primary_key=True)
    title = Column(String)
    date = Column(Integer)
    source = Column(Integer, ForeignKey("sources.id"))
  
    def __init__(file):
        self.name = name
        self.number = number
        self.team = team
    
    def __repr__(self):
        return "<Player('%s', '%s')>" % (self.name, self.number)


    class Sources(Base):
        __tablename__ = 'sources'

        id = Column(Integer, primary_key=True)
        source = Column(String)

    def __init__(self, name, number, team=None):
        self.name = name
        self.number = number
        self.team = team


    