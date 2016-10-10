from flask import Flask, request , redirect, url_for ,jsonify , session,  escape, request
from flask_restful import Resource, Api
from bson.objectid import ObjectId
from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from datetime import datetime
import os, uuid , random ,json ,math , validators

app = Flask(__name__)
api = Api(app)





class getreport(Resource):

	def __init__(self):
		pass

	def post(self):
		errors = []

	
		if len(errors) == 0:
			makeresponse = {
				'status':'true',
				'response':'response success'
				}

		else:
			makeresponse = {
				'status':'false',
				'response':'Some fields are missing (check data parameter in response)',
				'data':errors
			}
		return makeresponse


api.add_resource(getreport, '/registration')

if __name__ == '__main__':
	app.secret_key = 'FDSFDHFewsdf45$^$%^@#$@$$%#$YDSC-fdsfD^$$%^#2DX'
	app.run(debug=True)