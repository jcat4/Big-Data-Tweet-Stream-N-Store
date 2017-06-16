import tweepy
from dao.CredentialsDAO import CredentialsDAO

credentialsDAO = CredentialsDAO()

class MyStreamListener(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)