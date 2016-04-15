import simplejson
import requests
import praw
import pprint as pp
import collections
import wget
import time
import urllib3

subreddit = [
	'askreddit',
	'funny',
	'todayilearned',
	'pics',
	'science',
	'worldnews',
	'iama',
	'announcements',
	'videos',
	'gaming'	
]

file_url = [
	'http://www.reddit.com/r/askreddit.json',
	'http://www.reddit.com/r/funny.json',
	'http://www.reddit.com/r/todayilearned.json',
	'http://www.reddit.com/r/pics.json',
	'http://www.reddit.com/r/science.json',
	'http://www.reddit.com/r/worldnews.json',
	'http://www.reddit.com/r/iama.json',
	'http://www.reddit.com/r/announcements.json',
	'http://www.reddit.com/r/videos.json',
	'http://www.reddit.com/r/gaming.json'
]

# for x in file_url:
# 	time.sleep(10)
# 	file_name = wget.download(x)
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
http = urllib3.PoolManager(10, headers=user_agent)

for i in range(0,10):
	r = http.urlopen('GET', file_url[i])
	with open(subreddit[i]+'.json', 'wt') as out:
		pp.pprint(r.data, stream=out)


# file_name = wget.download('http://www.reddit.com/r/askreddit.json')

# r = praw.Reddit(user_agent="test")
# r.config.store_json_result=True
# user = r.get_redditor("test")

# gen = user.get_submitted(limit=1000)
# karma_by_subreddit = {}
# for thing in gen:
#      subreddit = thing.subreddit.display_name
#      karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
#                                      + thing.count)

# stuff = r.request_json("Https://www.reddit.com/r/askreddit/")
