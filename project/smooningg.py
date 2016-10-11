import json, urllib, requests

class url(object):

	def __init__(self):
		self.geturl()

	def geturl(self):

		keyword = raw_input('Enter the URL::')
		keyword = keyword.replace("www","")
		keyword = keyword.replace("https://","")
		keyword = keyword.replace(".com/","")

		#print keyword
		token="EAACEdEose0cBAOtOmNcyajumnHTvvw8EPCpuLrNl0mitoVRYjYnm1QU3ZCeLVk0OcczHNECCJRnSKmBVhfHLh9uyr8z2y35XcwWNuwViglyBFbPwyHw4OLtXZBzb2PJqFzBJP5mzgfSfYo5ROfjS11M9CNUdvIkEvLgZBtokAZDZD"
		typee="page"


		url=('https://graph.facebook.com/search?'
			'q=%s'
			'&type=%s'
			'&access_token=%s') % (keyword, typee, token)
		response=urllib.urlopen(url)

		data=json.loads(response.read())
		print data
		name= data['data'][0]['name']
		idd = data['data'][0]['id']
		print "NAME::"+name
		print "idd::"+idd

if __name__=="__main__":
	obj =url()
