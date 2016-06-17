# Plan?


##### Reddit scraper (I believe we have something relevant?)

#

1. Crawling some subreddits' (less work if manually selected ) posts (hot posts? all posts?) for few pages
  - read into threads and comments -> json
  
2. Crawling some active users/mods  (less work if manually selected ) from those subreddits
  - grab data from user side -> json
  
3. Those json should span the entire data range that we need (some data should be overlapped from 1 and 2 ?) 
#



##### Parser / Postprocess 
- Data sorting towards desired tables that we need
- json-sql library/webtool
- Processing might involves some of the functional dependencies work that we can use in report?


##### Misc
- dataflow: redditapi -> scrapers -> jsons -> processing  -> sql code for building database
- hosting sql on https://aws.amazon.com/



##### Proposal feedback: Interesting and practical application. Please see the comments below.
1. Please also provide relational schema.
2. If user is identified by username, how to deal with the situation that multiple users have same username? Please consider userID as primary key.
3. Can you explain what are link karma and comment karma and the difference between them?
4. Can multiple users be the moderators of a single subreddits?
5. You cannot link Users and Trophy directly in ER diagram. Put a many-to-many relation between them. To make it clear, it's better to put relations between every pair of entities, even for 1-to-many and 1-to-1 relations.
6. Consider full participations between: Posts and Users, Posts and Subreddit, Comments and Posts, Subscribes and Subreddit, etc.
