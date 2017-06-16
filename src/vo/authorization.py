import tweepy
from dao.CredentialsDAO import CredentialsDAO

class Authorization(object):
  
  def __init__(self):
    print("Authorization object created")
    self.authorize()
    
  def authorize(self):
    credentialsDAO = CredentialsDAO()
    auth = tweepy.OAuthHandler(credentialsDAO.getToken(), credentialsDAO.getSecret())
    auth.set_access_token(credentialsDAO.getAccessToken(), credentialsDAO.getAccessSecret())
    self.api = tweepy.API(auth)
    print("Stream credentials accepted")
    
  def getAPI(self):
    return self.api