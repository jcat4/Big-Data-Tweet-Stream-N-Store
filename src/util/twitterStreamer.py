import tweepy
from dao.CredentialsDAO import CredentialsDAO

credentialsDAO = CredentialsDAO()

class MyStreamListener(tweepy.StreamListener):
  
  def __init__(self):
    print("Streamer object created")
    self.consumer_token = credentialsDAO.getToken()
    self.consumer_secret = credentialsDAO.getSecret()
    print("Stream credentials recieved")
  
  def on_status(self, status):
    print(status.text)