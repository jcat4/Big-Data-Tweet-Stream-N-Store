import pymongo
from pymongo import MongoClient

import abc
from dao.DAOBase import DAOBase

class UsersDAO(DAOBase):
  
  connection = MongoClient()
  usersDAO = connection.StreamNStore.users
  
  def __init__(self):
    print("UsersDAO object created")
    
  def updateCollection(self, status):
    data = {
      "name":     str(status.author.screen_name),
      "id":       str(status.author.id),
      "location": str(status.author.location),
      "language": str(status.author.lang),
      "timezone": str(status.author.time_zone)
    }
    self.usersDAO.update_one(
      {"id": str(status.author.id)}, 
      {"$set": data}, upsert = True)
    
  def getNumOfDocs(self):
    return self.usersDAO.count()