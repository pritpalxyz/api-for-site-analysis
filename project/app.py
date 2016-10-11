from flask import Flask, request , redirect, url_for ,jsonify , session,  escape, request
from flask_restful import Resource, Api
from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from datetime import datetime
import os, uuid , random ,json ,math , validators
from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2, re, json , urllib , requests
from pprint import pprint

app = Flask(__name__)
api = Api(app)

class getreport(Resource):

	def __init__(self):
		self.TOKEN = """EAACEdEose0cBAMizvPd0ngoq5k3u2ZAuSZCPoDPTkwRKup524Y4QS5UujlvLvBov5P6cczuNluRdrzmjQBlhO6ZBvUkZB67KfFV96qk904sQ0i8ktH8FzXGcYOEFnaP1VCqXVa7gaZCpAZBflMRxKcZAjTSkuO0FDq4Dtn0KoMsXwZDZD"""

	def getfacebookpage(self,sitename):
		req = Request(sitename)
		html_page = urllib2.urlopen(req)
		soup = BeautifulSoup(html_page,"lxml")
		outputurl = None
		for link in soup.findAll('a'):
			uurl = link.get('href')
			try:
				if "facebook.com" in uurl:
					outputurl = uurl
			except:
				outputurl = None
		return outputurl

	def searchPageOnFacebook(self,name):
		name = name.title()
		url=('https://graph.facebook.com/search?'
			'q=%s'
			'&type=page'
			'&access_token=%s') % (name,self.TOKEN)
		response=urllib.urlopen(url)

		try:
			data=json.loads(response.read())
			idd = data['data'][0]['id']
			return idd
		except:
			return None

	def getPageAllInfo(self,IDD):
		api_endpoint = "https://graph.facebook.com/v2.8/"
		fb_graph_url = api_endpoint+IDD+"?fields=id,link,name,cover,feed,fan_count,username&access_token="+self.TOKEN
		response = requests.get(fb_graph_url)
		data = json.loads(response.content)
		return data

	def makejsonfromdict(self,data):
		try:name = data['name']
		except:name = ""
		try:url = data['link']
		except:url = ""
		try:cover = data['cover']
		except:cover = []
		try:likes = data['fan_count']
		except:likes = ""
		try:last_update = data['feed']['data'][0]['created_time']
		except:last_update = ""
		facebook = {
					"pageexist":1,
					"name":name,
					"url":url,
					"cover":cover,
					"likes":likes,
					"last_update":last_update
					}
		return facebook


	def post(self):
		errors = []
		try:websitename = request.form['site']
		except:errors.append('site')

	
		if len(errors) == 0:
			print websitename
			facebookpage = self.getfacebookpage(websitename)
			if facebookpage is not None:
				print facebookpage
				faecbookpageNAME = facebookpage.split("/")[3].split("?")[0]
				print faecbookpageNAME
				data = self.getPageAllInfo(faecbookpageNAME)
				facebook = self.makejsonfromdict(data)
			else:
				strippedSiteName = websitename.replace("www.","").split("//")[1].split(".")[0]
				makeresp = self.searchPageOnFacebook(strippedSiteName)
				if makeresp is not None:
					data = self.getPageAllInfo(makeresp)
					facebook = self.makejsonfromdict(data)
				else:
					facebook = {}

			makeresponse = {
				'status':'true',
				'response':'response success',
				'facebook':facebook
				}

		else:
			makeresponse = {
				'status':'false',
				'response':'Some fields are missing (check data parameter in response)',
				'data':errors
			}
		return makeresponse


api.add_resource(getreport, '/get-report')

if __name__ == '__main__':
	app.secret_key = 'FDSFDHFewsdf45$^$%^@#$@$$%#$YDSC-fdsfD^$$%^#2DX'
	app.run(debug=True)
