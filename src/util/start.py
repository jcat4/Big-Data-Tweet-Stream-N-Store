from .twitterStreamer import MyStreamListener
from vo.authorization import Authorization

streamer = MyStreamListener()
auth = Authorization()
#streamer = tweepy.Stream(streamer.getAPI().auth, listner=)