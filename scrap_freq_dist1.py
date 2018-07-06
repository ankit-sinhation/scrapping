#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords
import nltk
import matplotlib

#reading data from URL
# YOUTUBE
web=urllib.request.urlopen('https://www.youtube.com/')
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
'''
print (tokenized)
'''
print (" ")
print ("YOUTUBE SOURCE CODE LENGTH:")
print (len(tokenized))

#applying frequency distribution counter:
word_count=nltk.FreqDist(tokenized)
#plotting the graph:
word_count.plot(15)


