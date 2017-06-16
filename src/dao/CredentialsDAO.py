import pymongo
from pymongo import MongoClient

class CredentialsDAO(object):
  
  connection = MongoClient()
  credentialsDAO = connection.StreamNStore.credentials
  
  def __init__(self):
    print("Credentials DAO created")

  def getToken(self):
    return self.credentialsDAO.find_one({}, {"key": 1})["key"]
  
  def getSecret(self):
    return self.credentialsDAO.find_one({}, {"secret": 1})["secret"]