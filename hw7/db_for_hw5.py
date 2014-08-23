import sqlalchemy
import csv
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#To avoid problems with the format, it's required to make sure that the encoding is utf
#This is needed to apply the function unicode further

reload(sys)
sys.setdefaultencoding('utf-8')

#global varaible to automatically increase the ids in the scrapes table
scrapes_base=-1


#Connect to the local database, can use :memory: to just try it out in memory
#Make sure to delete the database before running the code again
#There must be NO database when you run this code
engine = sqlalchemy.create_engine('sqlite:///hw5_db.db', echo=False)

Base = declarative_base() 

#Define some schemas
class Source(Base):
        __tablename__ = 'sources'
        
        id = Column(Integer, primary_key=True)
        name=Column(String)
        link=Column(String)
        date = Column(String)
        
        def __init__(self,id,name,link,date):
            self.id = id
            self.name = name
            self.link = link
            self.date=date

        def __repr__(self):
            return "<Sources('%s', '%s')>" % (self.link, self.date)

class Scrape(Base):
    __tablename__ = 'scrapes'
  
  #Have an ID column because player attributes (name, etc) are not unique
    id = Column(Integer, primary_key=True)
    link = Column(String)
    text = Column(String)
    blog = Column(String)
    source = Column(Integer, ForeignKey("sources.id"))
   
  
    def __init__(self,text,link,blog,source):
        global scrapes_base 
      
        scrapes_base+=1
        self.id = scrapes_base
        self.text = text
        self.blog = blog
        self.link = link
        self.source = source

    def __repr__(self):
        return "<Scrapes('%s', '%s', '%s')>" % (self.link, self.blog, self.source)


Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()
'''
source = Source(1,"Blog of Supersopic","http://supersonic.wordpress.com","08/20/2014")
session.add(source)
session.commit()

c=0

with open('links_store.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if (c==0):
            c=1
            continue
        if (row[0]==None): continue
        session.add(Scrape(unicode(row[0]),unicode(row[1]),unicode(row[2]),1))
        session.commit()

#The tables have been created       
'''

for scrape, source in session.query(Scrape,Source).order_by(Scrape.id):
  print scrape.text, scrape.link, source.name, source.date


