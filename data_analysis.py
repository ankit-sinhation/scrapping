#!/usr/bin/python3

import tweepy
#defining consumer key and secret
#making connection with twitter api
c_key="7yyvLE5vaOjXg9mZwfaqKaGGq"

c_sec="2tme8Ijx9JLYYsn7619BBmInZaWobYezdCjpibld1C6DGkSGhN"
#token key & secret 
#to search & get information u need to use token
t_key="1014803225210441728-5CN0MXhld6NsBww3fjNSwaZyrH3Del"

t_sec="HXYF7GhQI3GTLsmRudLDk6sVHEwnSdP89SmOnpIXxOm9j"

#connecting twitter API
auth=tweepy.OAuthHandler(c_key,c_sec)
##print(dir(auth))

#setting & sending token key and secret
auth.set_access_token(t_key,t_sec)

#now accessing API
api_connect=tweepy.API(auth)

#searching data from the twitter
topic=input("Enter The Topic: ")
result=api_connect.search(topic)

##print (result)

for i in result :
    print (i.text)











