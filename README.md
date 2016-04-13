# Plan?


##### Reddit scraper (I believe we have something relevant?)

#

1. Crawling some subreddits' (less work if manually selected ) posts (hot posts? all posts?) for few pages
  - read into threads and comments -> json
  #
2. Crawling some active users/mods  (less work if manually selected ) from those subreddits
  - grab data from user side -> json
  #
3. Those json should span the entire data range that we need (some data should be overlapped from 1 and 2 ?) 
#



##### Parser / Postprocess 
- Data sorting towards desired tables that we need
- Can primarily use Node.js with its json-sql library
- Processing might involves some of the functional dependencies work that we can use in report?


##### Misc
- dataflow: redditapi -> scrapers -> jsons -> processing  -> sql code for building database
- hosting sql on https://aws.amazon.com/free/ ?

