import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
    self.outputFile = open("output.txt", 'ab')
    self.status_count = 0
  
  def on_status(self, status):
    self.status_count += 1
    self.outputFile.write(self.getStatusInfo(status))
    print("wrote status", self.status_count)
    
  def setAPI(self, api):
    self.api = api
    
  def getStatusInfo(self, status): # implement geo enabled logic
    info = "Number: "     + str(self.status_count) + "\n" + \
           "author: "     + str(status.author.screen_name) + "\n" + \
           "text: "       + str(status.text) + "\n" + \
           "language: "   + str(status.author.lang) + "\n" + \
           "location: "   + str(status.author.location) + "\n" + \
           "time zone: "  + str(status.author.time_zone) + "\n" + \
           "created at: " + str(status.created_at) + "\n\n"
    return info.encode("UTF-8")
    