#I do this whole analysis with my new small blog, which is very empty so far. However, if it has more posts it would work the same

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
from datetime import *
import urllib2
from blog_classes import * 
import sys

#this is needed to avoid difficulties with the encoding. without this on windows the default is cp1251, which may get a lot trouble 
#while reading a file 
reload(sys)
sys.setdefaultencoding('utf-8')


order=-1
# What page? 
page_to_scrape = 'https://supers0nick.wordpress.com/'

# What info do we want? 
headers = ["Text", "Links","Related to a blogposting"]

# Where do we save info?


# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

#Here the difficulty, if to follow the task exactly, is that the links for time and comments are actually links themselves. 
#I get
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

#get the titles of the posts, they'll parsed further
headers=soup.findAll("h2",attrs={'class':'entry-title'})

#get the dates of the posts, they'll parsed further
dates=soup.findAll("span",attrs={'class':'entry-date'})
 
#get the "tag group" with the comments, they'll parsed further
comments=soup.findAll("span",attrs={'class':'comments-link'})

ls = blogposts()

for i in range(0,len(headers)):
    ls.append(blogpost(headers[i],dates[i],comments[i]))
	
ls.sort() 
  
headers = ["Link", "Title","Number of comments","Date"]
filename = "blog_store.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)          

for i in range(0,ls.len+1):
    csvwriter.writerow([ls.db[i].http,ls.db[i].title,ls.db[i].comment,ls.db[i].date])
       
readFile.close()       
