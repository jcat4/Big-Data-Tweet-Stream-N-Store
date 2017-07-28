import pymongo
from pymongo import MongoClient

import abc
from dao.DAOBase import DAOBase

class LanguagesDAO(DAOBase):
  
  connection = MongoClient()
  
  def __init__(self):
    print("TweetsDAO object created")
    
  def updateCollection(self, status):
    self.currentDAO = connection.StreamNStore[str(status.author.lang)]
    data = {
      "authorID":          str(status.author.id),
      "author_name":       str(status.author.screen_name),
      "language":          str(status.author.lang),
      "location":          str(status.author.location),
      "text":              str(status.text),
      "created_at":        str(status.created_at),
      "tweet_id":          str(status.id),
      "reply_to_tweet_id": str(status.in_reply_to_status_id),
      "reply_to_user_id":  str(status.in_reply_to_user_id_str)
    }
    self.currentDAO.insert(data)
    
  def getNumOfDocs(self):
    return self.currentDAO.count()