import tweepy

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
  
  def on_status(self, status):
    print(status.text)