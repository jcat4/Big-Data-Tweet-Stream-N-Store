import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
    self.outputFile = open("output.txt", 'ab')
  
  def on_status(self, status):
    #print(json.loads(status)["text"])
    self.outputFile.write((status.text + "\n").encode("UTF-8"))
    
  def setAPI(self, api):
    self.api = api
    