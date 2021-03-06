
from bs4 import BeautifulSoup

import csv 
from nltk.util import clean_html
import urllib2


page_to_scrape = 'https://petitions.whitehouse.gov/petitions'

# What info do we want? 
headers = ["Summary", "Signatures"]

# Where do we save info?
filename = "whitehouse-petitions.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract petitions on page
#petitions = soup.findAll("a", href=re.compile('^/petition'))
petitions = soup.findAll("div", attrs={'class':'title'})
print len(petitions)
for petition in petitions:
 # p = clean_html(str(petition.find("a")))
 p = (petition.find("a") )
 p = p.get_text()
 print p

signatures = soup.findAll("div", attrs={'class':'num-sig'})
print len(signatures)
for signature in signatures:
  s = signature.find("span", attrs={'class':'num'})
  s = s.get_text()
  #s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  print s

for i in range(20):
  petition = petitions[i]
#  p = clean_html(str(petition.find("a")))
  p = petition.find("a")
  signature = signatures[i]
  #s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  s = signature.find("span", attrs={'class':'num'})
  csvwriter.writerow([p, s])

readFile.close()