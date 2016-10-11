import urllib2
import json
from pprint import pprint
def get_page_data(page_id,access_token):

    api_endpoint = "https://graph.facebook.com/v2.8/search"
    fb_graph_url = api_endpoint+"?type=page&q=Smooning&fields=id,name&access_token="+access_token
    print fb_graph_url
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        print "ERROORRR"
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "Snapdeal" # username or id
token = "EAACEdEose0cBAMizvPd0ngoq5k3u2ZAuSZCPoDPTkwRKup524Y4QS5UujlvLvBov5P6cczuNluRdrzmjQBlhO6ZBvUkZB67KfFV96qk904sQ0i8ktH8FzXGcYOEFnaP1VCqXVa7gaZCpAZBflMRxKcZAjTSkuO0FDq4Dtn0KoMsXwZDZD"  # Access Token
page_data = get_page_data(page_id,token)
pprint(page_data)
# print "Page Name:"+ page_data['name']
# print "Likes:"+ str(page_data['likes'])
# print "Link:"+ page_data['link']