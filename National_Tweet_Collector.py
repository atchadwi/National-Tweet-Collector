import json, tweepy
from html.parser import HTMLParser
from contextlib import suppress

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

count = 0

class StdOutListener(tweepy.StreamListener):
   def on_data(self, data):
      global count
      decoded = json.loads(HTMLParser().unescape(data))
      if decoded.get('coordinates',None) is not None:
         coordinates = decoded.get('coordinates','').get('coordinates','')
         user = decoded.get('user','').get('screen_name', '')
         date = decoded.get('created_at','')
         with open("National_Tweets.txt", "a") as text_file:
            print((decoded['coordinates'], user, date), file=text_file)
         print((decoded['coordinates'], user, date))
         count += 1
      return True
   def on_error(self, status):
      print(status)

l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
stream = tweepy.Stream(auth, l)

while count < 3000000:
   with suppress(TypeError, ValueError, AttributeError):
      stream.filter(locations=[-125.0011, 24.9493, -66.9326, 49.5904])
