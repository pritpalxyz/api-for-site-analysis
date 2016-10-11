from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2, re, json

class url(object):

	def __init__(self):
		self.geturl()

	def geturl(self):
		url = raw_input('Enter the URL::')
		req = Request(url)

		html_page = urllib2.urlopen(req)
		soup = BeautifulSoup(html_page,"lxml")
		for link in soup.findAll('a'):
			uurl = link.get('href')
			try:
				if "facebook.com" in uurl:
					print uurl
			except:
				pass

if __name__=="__main__":
	obj =url()
