import pymongo
from pymongo import MongoClient

import abc
from dao.DAOBase import DAOBase

class TweetsDAO(DAOBase):
  
  connection = MongoClient()
  tweetsDAO = connection.StreamNStore.tweets
  
  def __init__(self):
    print("TweetsDAO object created")
    
  def updateCollection(self, status):
    data = {
      "authorID":           str(status.author.id),
      "author_name":        str(status.author.screen_name),
      "language":           str(status.author.lang),
      "location":           str(status.author.location),
      "text":               str(status.text),
      "created_at":         str(status.created_at),
      "tweet_id":           str(status.id),
      "reply_to_tweet_id":  str(status.in_reply_to_status_id),
      "reply_to_user_id":   str(status.in_reply_to_user_id_str),
      "reply_to_user_name": str(status.in_reply_to_screen_name)
    }
    self.tweetsDAO.insert(data)
    
  def getNumOfDocs(self):
    return self.tweetsDAO.count()
  
  def getSizeOfDB(self):
    return (self.connection.StreamNStore.command("dbstats")["dataSize"] / 1000000) 