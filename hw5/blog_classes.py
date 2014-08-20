from datetime import *
from externalfun import *

order=-1

class blogpost():
    def __init__(self,title,date,comments):
        global order
        self.comment=parse_comments(comments.get_text())
        self.title=title.get_text()
        self.http=(title.findAll('a')[0])['href']
        self.date=make_date(date)
        self.order=order+1

    @staticmethod
    def zero_counter(self):
        global order
        self.order=order=-1


class blogposts():
    def __init__(self):
        self.db=[]
        self.len=-1

    def append(self,blog):
        self.db.append(blog)
        self.len+=1

    #bubble sort based on date field
    def sort(self):
       for i in range(0,self.len):
            for j in range(0,self.len-i):
               if (self.db[j+1].date<=self.db[j].date):
                    t = self.db[j]
                    self.db[j]= self.db[j+1]
                    self.db[j+1] =t
