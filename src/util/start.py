import tweepy

from .twitterStreamer import MyStreamListener
from vo.authorization import Authorization

# make a command line param?
searchTerm = "memes"

streamer = MyStreamListener()
auth = Authorization()
streamer.setAPI(auth.getAPI())

print("\nStoring all tweets regarding ", searchTerm, "...")
stream = tweepy.Stream(auth = auth.getAuth(), listener = streamer)
stream.filter(track=[searchTerm], async = True)