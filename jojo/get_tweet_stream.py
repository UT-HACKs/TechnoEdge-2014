# -*- coding:utf-8 -*-
import twitter

### Constants                                                                                                                                                     
oath_key_dict = {
    "consumer_key": "",
    "consumer_secret": "",
    "access_token": "",
    "access_token_secret": ""
}
"""
import json, urllib2, oauth2 as oauth
bound = ["139.694123","35.683192","139.709272","35.694555"]
def check_bound(item,bound):
        if item['coordinates']==None:
                return False
        tmp = item['coordinates']['coordinates']
        if float(bound[0])<=tmp[0] and tmp[0]<=float(bound[2]) and float(bound[1])<=tmp[1] and tmp[1]<=float(bound[3]):
                return True
        else:
                return False


consumer = oauth.Consumer(key = oath_key_dict["consumer_key"], secret = oath_key_dict["consumer_secret"])
token = oauth.Token(key = oath_key_dict["access_token"], secret = oath_key_dict["access_token_secret"])
 
#エンドポイントURL
#https://dev.twitter.com/docs/api/1.1/get/statuses/sample あたり参照
#trackなどの条件を指定して絞り込むのも好いかも
url = 'https://stream.twitter.com/1.1/statuses/filter.json'
params = {'track': 'love'}
#params = {'locations': '139.694123,35.683192,139.709272,35.694555'}
request = oauth.Request.from_consumer_and_token(consumer, token, http_url=url, parameters=params)
request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
res = urllib2.urlopen(request.to_url())
print "ready"
for r in res:
    data = json.loads(r)
 
    try:
        if check_bound(data,bound):
            print '==============================='
            print data['user']['screen_name']
            print data['text']
            print data['coordinates']
 
    except:
        #たまーにデリートフラグのついたツイートが流れてくるので（？）適当に受け流す 詳しくは未調査
        pass



"""
api = twitter.Api(base_url="https://api.twitter.com/1.1",
                      consumer_key=oath_key_dict["consumer_key"],
                      consumer_secret=oath_key_dict["consumer_secret"],
                      access_token_key=oath_key_dict["access_token"],
                      access_token_secret=oath_key_dict["access_token_secret"])
def check_bound(item,bound):
        if item['coordinates']==None:
                return False
        tmp = item['coordinates']['coordinates']
        if float(bound[0])<=tmp[0] and tmp[0]<=float(bound[2]) and float(bound[1])<=tmp[1] and tmp[1]<=float(bound[3]):
                return True
        else:
                return False

bound = ["139.694123","35.683192","139.709272","35.694555"]
trace =  ["technoedge"]

for item in api.GetStreamFilter(track = trace):
        print '---------------------'
        if 'text' in item:# and check_bound(item,bound):
            print (item['id_str'])
            print (item['text'])
            print (item['coordinates'])            
