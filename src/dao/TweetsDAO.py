import pymongo
from pymongo import MongoClient

class TweetsDAO(object):
  
  connection = MongoClient()
  tweetsDAO = connection.StreamNStore.tweets
  
  def __init__(self):
    print("TweetsDAO object created")
    
  def updateTweets(self, status):
    data = {
      "authorID":          str(status.author.id),
      "text":              str(status.text),
      "created_at":        str(status.created_at),
      "tweet_id":          str(status.id),
      "reply_to_tweet_id": str(status.in_reply_to_status_id),
      "reply_to_user_id":  str(status.in_reply_to_user_id_str)
    }
    self.tweetsDAO.insert(data)
    
  def getNumOfDocs(self):
    return self.tweetsDAO.count()