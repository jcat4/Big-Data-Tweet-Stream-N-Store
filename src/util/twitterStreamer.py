import tweepy

from dao.UsersDAO import UsersDAO
from dao.TweetsDAO import TweetsDAO

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
    self.usersDAO = UsersDAO()
    self.tweetsDAO = TweetsDAO()
  
  def on_status(self, status):
    print("Got Status")
    self.usersDAO.updateUsers(status)
    self.tweetsDAO.updateTweets(status)
    
  def setAPI(self, api):
    self.api = api    