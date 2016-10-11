import urllib2
import json
# from pprint import pprint
def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "Snapdeal" # username or id
token = "EAACEdEose0cBAJHS1obKZBZB8lfxZCMxhF0HR52id64SgXrsk2TdsbV4NlubymL6VEYkSBwjIw7KT1t0ZC0kikMdulpamIqNZBw0MbIDUjfiSrx97j9DeWbMb9F8HZAuzOD8POuDuNne3zIwtIz6uJHokoY6hciScfhgKXOwGhLgZDZD"  # Access Token
page_data = get_page_data(page_id,token)
# pprint(page_data)
print "Page Name:"+ page_data['name']
print "Likes:"+ str(page_data['likes'])
print "Link:"+ page_data['link']