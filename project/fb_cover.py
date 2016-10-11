import json, urllib, requests

token = "EAACEdEose0cBAPArEQvx4rufjakmTOyddQEQsb4Dn7z0JzE5pV7fK15VWWUjhs2y2jDvaX6iNH1YYGoZA9mkS9pb2fZBugsuZBZCr6UJwUwfBBZCSaMAjTZA3r1tbFnMPlEnqvOc73OrEQfpLbdUyeMTrnToFqMDkMxuDFZA9R9gQZDZD"  # Access Token
iid = "303858136365695"

url=('https://graph.facebook.com'
		'/%s'
		'/albums?access_token=%s') % (iid, token)
response=urllib.urlopen(url)
data=json.loads(response.read())

cvr_pic = data['data'][0]['link']
updated = data['data'][0]['updated_time']
#print data    
print "Cover-Photo Link::"+cvr_pic
print "Latest Post updated::"+updated