import time
import tweepy
from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2, re, json


class getreport(object):

	def __init__(self):
		self.consumer_key = """LWZKQrOEjvIS3BhXfBlBx1IIJ"""

		self.consumer_secret = """8In55F4G4vBI5g6Y60QF93QV2P0C8at1ChP7xDaPCiIkoyvY7k"""

		self.access_token = """786435230529757184-xxnH7kGswhWPUZvzR5bv6W55opZX3vD"""

		self.access_token_secret = """mOv9ewyubolRmk5IiUqrhwWxu2L7ALAoJOyhEAazxoa7s"""
		self.get_user_detail()
		self.get_last_tweet()

	def get_user_detail(self):

		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		api = tweepy.API(auth)	
		user = api.get_user("snapdeal")  
		
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

	def get_last_tweet(self):
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		api = tweepy.API(auth)	
		user = api.get_user("snapdeal")  

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

if __name__ == '__main__':
	obj=getreport()
