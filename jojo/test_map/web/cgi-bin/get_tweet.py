# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json

### Constants                                                                                                                                                     
oath_key_dict = {
    "consumer_key": "btaFCVBWqLUkyuqjJVK32yzoq",
    "consumer_secret": "0kCjsoKCcyIAqIMXSOapAzAkFkm2KbMmTBdtL5JrNs04Tao3NG",
    "access_token": "1404461461-vwwdfmQwjm0pSpoedbeW796gMjbIWoD6qQZLT5e",
    "access_token_secret": "YBRHBPER2nVlohtg3rrGgfK4N6i7yRnKH0GibXeF4daix"
}


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath


def tweet_search_by_location(lng,lat,rad,oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": unicode(search_word),
        "lang": "ja",
        "result_type": "recent",
        "count": "100",
        
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets
