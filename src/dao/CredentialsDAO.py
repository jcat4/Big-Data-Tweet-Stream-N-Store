import pymongo
from pymongo import MongoClient

class CredentialsDAO(object):
  
  connection = MongoClient()
  credentialsDAO = connection.StreamNStore.credentials
  
  def __init__(self):
    print("Credentials DAO created")

  def getKey(self):
    return credentialsDAO.find_one({}, {"key": 1})["key"]
  
  def getToken(self):
    return credentialsDAO.find_one({}, {"secret": 1})["secret"]