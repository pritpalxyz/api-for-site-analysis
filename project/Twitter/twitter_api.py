import time
import tweepy
from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2, re

url = raw_input('Enter the URL::')
req = Request(url)
html_page = urllib2.urlopen(req)
soup = BeautifulSoup(html_page,"lxml")
for link in soup.findAll('a'):
	uurl = link.get('href')
	try:
		if "twitter.com" in uurl:
			print "Twitter Page URL:: "+uurl
	except:
		pass

key = url.replace("www.","")
key = key.replace("https://","")
key = key.replace(".com/","")
# print key




auth = tweepy.OAuthHandler("LWZKQrOEjvIS3BhXfBlBx1IIJ", 	"8In55F4G4vBI5g6Y60QF93QV2P0C8at1ChP7xDaPCiIkoyvY7k")
auth.set_access_token("786435230529757184-xxnH7kGswhWPUZvzR5bv6W55opZX3vD",  "mOv9ewyubolRmk5IiUqrhwWxu2L7ALAoJOyhEAazxoa7s")

api = tweepy.API(auth)

user = api.get_user(key)  
# key = value stripped from url
print "---------------TWITTER PAGE DETAILA--------------------------"
print "User id: " + user.id_str
print "User Name: " +user.name
print "Description: " + user.description
print "Language: " + user.lang
print "Account created at: " + str(user.created_at)
print "Location: " + user.location
print "Time zone: " + user.time_zone
print "Number of tweets: " + str(user.statuses_count)
print "Number of followers: " + str(user.followers_count)
print "Following: " + str(user.friends_count)
print "A member of " + str(user.listed_count) + " lists."


statuses = api.user_timeline(id = user.id, count = 1)
for status in statuses:
	print "---------------LATEST POST DETAILS--------------------------"
	print "Tweet id: " + status.id_str
	print status.text
	print "Retweet count: " + str(status.retweet_count)
	print "Favorite count: " + str(status.favorite_count)
	print status.created_at
	print "Status place: " + str(status.place)
	print "Source: " + status.source
	print "Coordinates: " + str(status.coordinates)
	time.sleep(1)

posts = api.user_timeline(id = user.id, count = 200)
for post in posts:
	print "---------------LAST YEAR POST DETAILS--------------------------"
	print post.created_at
	time.sleep(1)