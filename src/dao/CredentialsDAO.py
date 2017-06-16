import pymongo
from pymongo import MongoClient

class CredentialsDAO(object):
  
  connection = MongoClient()
  credentialsDAO = connection.StreamNStore.credentials
  
  def __init__(self):
    print("Credentials DAO created")

  def getToken(self):
    return self.credentialsDAO.find({})[0]["token"]
  
  def getSecret(self):
    return self.credentialsDAO.find({})[0]["secret"]
  
  def getAccessToken(self):
    return self.credentialsDAO.find({})[1]["accessToken"]
  
  def getAccessSecret(self):
    return self.credentialsDAO.find({})[1]["accessSecret"]