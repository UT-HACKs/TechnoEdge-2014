# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json
import serial
import time
import re
### Constants                                                       
consumer_key = ""
consumer_secret = ""

oath_key_dict = {
    "consumer_key": "btaFCVBWqLUkyuqjJVK32yzoq",
    "consumer_secret": "0kCjsoKCcyIAqIMXSOapAzAkFkm2KbMmTBdtL5JrNs04Tao3NG",
    "access_token": "1404461461-gszluwE5vDm64lmb4LRjV1WdS6BhVpXzVFXaOXm",
    "access_token_secret": "Aclgyk7gmQYjxnOxCETRtxPaFArzloJfLHW3wfWtfxxj3"
}

def post_rep(tweet,oath_key_dict,text):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    tweet_text = '@'+tweet[u'user'][u'screen_name']+" "+text+" "+str(tweet[u'id'])
    print str(tweet[u'id'])
    params = { "status": tweet_text,"in_reply_to_status_id": str(tweet[u'id'])}
    oath = create_oath_session(oath_key_dict)
    responce = oath.post(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
    else:
        print "post successed"

def tweet_in_hawaii(oath_key_dict):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = { "status": 'ハワイなう',
               "lat":"21.278859",
               "long":"-157.827335",
               "display_coordinates":"true"
               }
    oath = create_oath_session(oath_key_dict)
    responce = oath.post(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
    else:
        print "post successed"
    

### Functions                                                                                                                                                     
def main():
    tweets = tweet_search(u"technoedge", oath_key_dict)
    count = 0
    for tweet in tweets["statuses"]:
            print tweet[u'coordinates']
            print tweet[u'user'][u'name']
            print tweet[u'text']
            if tweet[u'user'][u'name'] == "LY9988":
                post_rep(tweet,oath_key_dict,u"テスト成功！")
    print float(count)/len(tweets["statuses"])
    print len(tweets["statuses"])
    
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word.decode("utf-8"),
        "result_type": "recent",
        "count": "100"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

def new_tweet_search(search_word, since_id,oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word.decode("utf-8"),
        "result_type": "recent",
        "count": "100",
        "since_id":since_id.decode("utf-8")
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets


def tweet_search_by_user(user_id, oath_key_dict):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?"
    params = {
        "screen_name": unicode(user_id),
        "result_type": "recent",
        "count": "15"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

def tweet_search_by_screen_name(screen_name, oath_key_dict):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?"
    params = {
        "screen_name": unicode(screen_name),
        "result_type": "recent",
        "count": "15"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

def get_technoedge_tweet(screen_name,oath_key_dict):
    ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
    #newest_tweets = tweet_search("@"+screen_name,oath_key_dict)
    #since_id = newest_tweets[u'statuses'][0]["id"]
    newest_tweets = tweet_search_by_screen_name(screen_name,oath_key_dict)
    since_id = newest_tweets[0]["id"]
    while(1):
        #tweets = tweet_search("@"+screen_name,oath_key_dict)
        #newest_id = tweets[u'statuses'][0]["id"]
        tweets = tweet_search_by_screen_name(screen_name,oath_key_dict)
        newest_id = tweets[0]["id"]
        print "updated"
        if(newest_id>since_id):
            print "aaa"
            since_id=newest_id
            #text = tweets[u'statuses'][0]["text"]
            text = tweets[0]["text"]
            if("on" in text  or u"オン" in text):
                if(u"青" in text):
                    ser.write("q")
                else:
                    ser.write("o")
            if("off" in text or u"オフ" in text):
                if(u"青" in text):
                    ser.write("r")
                else:
                    ser.write("p")
        time.sleep(8)
    ser.close()
    
                
    
    
