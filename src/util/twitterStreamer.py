import tweepy
import sys
from sys import stdout

from dao.UsersDAO import UsersDAO
from dao.TweetsDAO import TweetsDAO

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
    self.usersDAO = UsersDAO()
    self.tweetsDAO = TweetsDAO()
  
  def on_status(self, status):
    self.usersDAO.updateUsers(status)
    self.tweetsDAO.updateTweets(status)
    sys.stdout.write("Users: %d\t" % (self.usersDAO.getNumOfDocs()))
    sys.stdout.write("Tweets: %d\t" % (self.tweetsDAO.getNumOfDocs()))
    sys.stdout.write("DB Size: %.2f MB\r" % (self.tweetsDAO.getSizeOfDB()))
    sys.stdout.flush()
    
  def setAPI(self, api):
    self.api = api    