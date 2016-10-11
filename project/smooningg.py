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
		token = "EAACEdEose0cBAMizvPd0ngoq5k3u2ZAuSZCPoDPTkwRKup524Y4QS5UujlvLvBov5P6cczuNluRdrzmjQBlhO6ZBvUkZB67KfFV96qk904sQ0i8ktH8FzXGcYOEFnaP1VCqXVa7gaZCpAZBflMRxKcZAjTSkuO0FDq4Dtn0KoMsXwZDZD"  # Access Token
		typee="page"

		keyword = keyword.title()
		url=('https://graph.facebook.com/search?'
			'q=%s'
			'&type=%s'
			'&access_token=%s') % (keyword, typee, token)
		print url
		response=urllib.urlopen(url)

		data=json.loads(response.read())
		name= data['data'][0]['name']
		idd = data['data'][0]['id']
		print "NAME::"+name
		print "idd::"+idd

if __name__=="__main__":
	obj =url()
