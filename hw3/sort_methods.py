from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
from datetime import *
import urllib2 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#this is needed to avoid difficulties with the encoding. without this on windows the default is cp1251, which may get a lot trouble 
#while reading a file 

order=-1
# What page? 
page_to_scrape = 'https://supers0nick.wordpress.com/'

# What info do we want? 
headers = ["Text", "Links","Related to a blogposting"]

# Where do we save info?

filename = "blog_log.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

#Here the difficulty, if to follow the task exactly, is that the links time and comments are actually links themselves. 
#While everything related to one blogpost is contained within div tag.
#What I would do (this is one of the approaches to this situations, obviously): 
#1) I will output all links and their titles (possible that some of them are repetitive or/and have no title) in a file links_store.csv
#each link will have a flag is_post, if this is one of the links related to a post (comments, date, post header)
#2) Afterwards I create another file for the blogposts,blog_store.csv, where I put 
#link | post title | number of comments | date of creation
#the entities are to be sorted in the chronological order

#1
links = soup.findAll("a")

filename = "links_store.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)


for l in links:
	name = l.get_text()
	address = l['href']
	post=""
	#the trick is that this is a new blog and a link leads to a post iff it contains the date in its address
	if "2014" in address: post="Yes"
	else: post="No"
	csvwriter.writerow([name, address,post])

readFile.close()

#2 
divs = soup.findAll("div")

#blogposting are of the class entry-title, which is defined on <h2>-level
#the general structure is:
#<div><h2 class ...>
# 

#get titles of the posts, they'll parsed in a common loop further
headers=soup.findAll("h2",attrs={'class':'entry-title'})

#get dates of the posts, they'll parsed in a common loop further
dates=soup.findAll("span",attrs={'class':'entry-date'})
 
#get the "tag group" with the comments
comments=soup.findAll("span",attrs={'class':'comments-link'})
 
def make_date(str):
    return  (datetime.strptime(str.get_text(), '%B %d, %Y')).strftime('%x')

def num(s):
    try:
        return int(s)
    except ValueError:
        return ""
	
def parse_comments(str):
    if (not isinstance(num(str[0]), int)): return 0
    i=0
    while str[i]!=" ": i+=1
    return(num(str[0:i]))       
   

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


ls = blogposts()

for i in range(0,len(headers)):
    ls.append(blogpost(headers[i],dates[i],comments[i]))
	
ls.sort()   
headers = ["Link", "Title","Number of comments","Date"]
filename = "blog_store.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)          

for i in range(0,ls.len):
    csvwriter.writerow([ls.db[i].http,ls.db[i].title,ls.db[i].comment,ls.db[i].date])
       
      
readFile.close()       
    #d.strftime('%x')
	
	#print date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
	#date = str(d.day)+"."+str(d.month)+"."+str(d.year)
	
	#print date
	#print headers[i]
	#print dates[i]
	#print comments[i]

print ls	
#divs = soup.findAll("a")
#print len(divs)
# Extract petitions on page
#petitions = soup.findAll("a", href=re.compile('^/petition'))
#petitions = soup.findAll("a", attrs={'class':'title'})
#posts = soup.findAll("h2",attrs={'class':'entry-title'})
#raw = soup.findAll("div")
#candidates = []
#candidates.append(raw)

		
			
#print len(posts)

#for link in links:
	#p=link.findAll("h2")
	#for p1 in p:
	#	print p1
	#print link
	
#for post in posts:
#	print post

'''
for link in links:
	if (link.findAll("h2",attrs={'class':'entry-title'})!=[]):
		print link.findAll("h2",attrs={'class':'entry-title'})

		'''
'''
links=soup.findAll("h2")
'''
'''
for link in links:
  link.findAll('a',href=True) 
  str= link.get_text() + ": " + link['href']
  print str
  name = link.get_text()
  address = link['href']
  csvwriter.writerow([name, address])
'''
'''
signatures = soup.findAll("div", attrs={'class':'num-sig'})
print len(signatures)
for signature in signatures:
  s =(signature.find("span", attrs={'class':'num'})).get_text()
  print s

for i in range(20):
  petition = petitions[i]
  p =(petition.find("a")).get_text()
  signature = signatures[i]
  s = (signature.find("span", attrs={'class':'num'})).get_text()
  csvwriter.writerow([p, s])
'''

