
import requests,praw,json,urllib,time
import pprint as pp


# total json requests: 10+10*25= 260 (10 subreddits, 25 posts in the first page for each)
# json from subreddits cover subreddit and post table
# json from posts cover posts and comments table

# user data would be grabbed using praw rather than accessing json

# these should cover our data range

# way to get trophies from user? praw doesn't seem to have it in redditor object

standard_init=['']*25; # we use 25 posts from a subreddit and up to 25 comments in each post


# alternatively we could put main func with this thing as an input, nah
subreddit_name_list = [
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

def myprint(x):
	return pp.pprint(x)


# final data stored in dicts

subreddits={'subredditname':[],'bannerlink':[],'iconlink':[],'mods':[],'subscribers':[],'useronline':[]}; 
#{'title': ['xx','xy'], 'id':..., 'bannerlink':..., 'iconlink':..., 'mods':...., 'subscribers':... (just number), 'useronline':...}

redditors={'name':[],'comment_karma':[],'link_karma':[]}
#,'trophies':[],'subscribes':[]}; 
#{'name': ['xx','xy'], 'id':...,(not needed) 'linkkarma':..., 'commentkarma':..., 'trophies':... (not yet), 'subscribes':...(no way to get this for arbitary users)}

posts={'postid':[],'title':[],'author':[],'post_content':[]'score':[],'gilded':[],'type':[],'subreddit':[]}; 
#{'title': ['xx','xy'], 'id':..., 'author':..., 'score/upvotes':..., 'gilded':... , 'type':...,'subreddit':...}

comments={'commentid':[],'postid':[],'comment_content':[],'author':[],'score':[],'gilded':[]}; 
# just get one layer from a post for now, it gets too complicated for nesting
#{'content': ['xx','xy'], 'selfid':..., 'parentid':..., 'author':..., 'score/upvotes':..., 'gilded':...}











# Initialization reddit session
r = praw.Reddit(user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
r.config.store_json_result=True

# tt = r.request_json("https://www.reddit.com/r/AskReddit/comments/4ewm01/whats_an_overused_askreddit_answer/")



# with open('data.json', 'w') as outfile:
#     json.dump(tt, outfile)




# run through 10 subreddits
def top_parse():
	for m in range(0,10):
		subreddit_parse(r.request_json('https://www.reddit.com/r/'+subreddit_name_list[m]), subreddit_name_list[m]);

# parse content for a subreddit
def subreddit_parse(subredditjson,subredditname):

	# also put an access time in data retrival: time.ctime()

	# get current subreddit object
	this = r.get_subreddit(subredditname);


	# get current subreddit data that we would store / subreddit data finished here
	#current_subreddit_bannerlink 
	subreddits['bannerlink'] += [this.banner_img];
	#current_subreddit_logolink 
	subreddits['iconlink'] += [this.icon_img];
	#current_subreddit_name 
	subreddits['mods'] += [subredditname];

	#current_subreddit_moderators 
	current_subreddit_moderators = (this.get_moderators())['json_dict']['children']; # return a list of redditors objects
	current_subreddit_moderator_names = ['']*len(current_subreddit_moderators);
	for k in range(0,len(current_subreddit_moderators)):
    	current_subreddit_moderator_names[k]=current_subreddit_moderators[k].name;
	subreddits['mods'] += [current_subreddit_moderator_names]

	#current_subreddit_subscribers 
	subreddits['subscribers'] += [this.subscribers];

	#current_subreddit_online 
	subreddits['useronline'] += [this.accounts_active];








	post_urls=standard_init; post_ids=standard_init; post_titles=standard_init; post_contents=standard_init;
	post_gilded=standard_init; post_ups=standard_init; post_authors=standard_init;


	for i in range(0,25):
		post_urls[i]=(vars(subredditjson['data']['children'][i]))['permalink']; #used for further parsing, not for data retrival

		post_ids[i]= (vars(subredditjson['data']['children'][i]))['id'];
		post_titles[i]= (vars(subredditjson['data']['children'][i]))['title'];
		post_authors[i]= (vars(subredditjson['data']['children'][i]))['author'];
		post_ups[i]= (vars(subredditjson['data']['children'][i]))['score'];
		post_domains[i]= (vars(subredditjson['data']['children'][i]))['domain'];
		post_gilded[i]= (vars(subredditjson['data']['children'][i]))['gilded'];
		post_contents[i]= (vars(subredditjson['data']['children'][i]))['selftext']; # could be none



	authornames=['']*len(post_authors);
	for k in range(0,len(post_authors)):
    	authornames[k]=post_authors[k].name;



	posts['postid']+=post_ids; posts['title']+=post_titles ;posts['gilded']+=post_gilded; posts['post_content']+=post_contents
	posts['author']+=authornames; posts['score']+=post_ups; posts['type']+=post_domains; posts['subreddit']+=[subredditname];

	user_parse(post_authors[i]);

	for p in range(0,25):
		post_parse(r.request_json(post_urls[p]),post_ids[p])




# postjson = r.request_json(post_urls[i])

# parse posts to get comments
def post_parse(postjson,pid):


	for w in range(0,len(postjson[1]['data']['children'])-1):

		comment_author=vars(postjson[1]['data']['children'][w])['author'];
		user_parse(comment_author);
		comments['author']+=[comment_author.name];

		comments['score']+=[vars(postjson[1]['data']['children'][w])['score']];
		comments['gilded']+=[vars(postjson[1]['data']['children'][w])['gilded']];
		comments['comment_content']+=[vars(postjson[1]['data']['children'][w])['body']];
		comments['commentid']+=[vars(postjson[1]['data']['children'][w])['id']];
		comments['postid']+=[pid];




# parse users relevant
def user_parse(redditorobject):
	redditors['comment_karma']+= [redditorobject.comment_karma];
	redditors['link_karma']+= [redditorobject.link_karma];
	redditors['name']+= [redditorobject.name];
