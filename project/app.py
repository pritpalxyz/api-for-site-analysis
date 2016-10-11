from flask import Flask, request , redirect, url_for ,jsonify , session,  escape, request
from flask_restful import Resource, Api
from bson.objectid import ObjectId
from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from datetime import datetime
import os, uuid , random ,json ,math , validators
from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2, re, json

app = Flask(__name__)
api = Api(app)





class getreport(Resource):

	def __init__(self):
		pass

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

	def post(self):
		errors = []
		try:websitename = request.form['site']
		except:errors.append('site')

	
		if len(errors) == 0:
			print websitename
			facebookpage = self.getfacebookpage(websitename)
			if facebookpage is not None:
				faecbookpageNAME = facebookpage.split("/")[3]
				print faecbookpageNAME

			makeresponse = {
				'status':'true',
				'response':'response success',
				'data':facebookpage
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
