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

engine = sqlalchemy.create_engine('sqlite:///hw6_db.db', echo=False)
Base = declarative_base() 

class User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        name=Column(String)
        nfollowers=Column(Integer)
        nfriends = Column(Integer)
        location = Column(String)
        crawl = Column(Integer, ForeignKey("crawls.id"))

        def __init__(self,id,name,nfollowers,nfriends,location,crawl):
            self.id = id
            self.name = name
            self.nfollowers = nfollowers
            self.nfriends=nfriends
            self.location = location
            self.crawl = crawl

        def __repr__(self):
            return "<User('%s', '%s')>" % (self.id, self.name)

class Crawl(Base):
    __tablename__ = 'crawls'
  
  #Have an ID column because player attributes (name, etc) are not unique
    id = Column(Integer, primary_key=True)
    base_user = Column(Integer)
    time = Column(String)
       
    def __init__(self,id,base_user,time):
       
        self.id = id
        self.base_user = base_user
        self.time = time

    def __repr__(self):
        return "<Scrapes('%s', '%s', '%s')>" % (self.id, self.base_user, self.time)

Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()


#this part creates the database, there's one crawl in it
'''

source = Crawl(1,206617660,"2014-08-23 16:41:41")
session.add(source)
session.commit()

with open('twitter_users.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (row[0]==None): continue
        session.add(User(unicode(row[0]),unicode(row[1]),unicode(row[2]),unicode(row[3]),unicode(row[4]),1))
        session.commit()

'''
#warning: reading the data base, always use  u.name.encode(sys.stdout.encoding, errors='replace') instead of just u.name
#certain friends have weird Scandinavian characters in their names that can't be displayed properly without an explicit 
#suppression of the error

for u, c in session.query(User,Crawl):
   print u.id, u.name.encode(sys.stdout.encoding, errors='replace'), u.nfollowers, u.nfriends, u.location, c.id, c.base_user
   