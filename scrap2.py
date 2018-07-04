#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords

#reading data from URL
# FACEBOOK
web=urllib.request.urlopen('https://www.facebook.com/')
#print or store HTML taged data
##print(web.read())
webdata=web.read()

#applying soup
souped=BeautifulSoup(webdata,'html5lib')

#if you want to print souped source of HTML:
##print(souped)

#only text extraction
text_data=souped.get_text()
##print (text_data)

tokenized=[i for i in text_data.split() if i.lower not in stopwords.words('english')]

print (tokenized)
print (" ")
print ("FACEBOOK SOURCE CODE LENGTH:")
print (len(tokenized))


