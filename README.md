# python-spider-mongo

This spider crawls foxnews.com and gets articles by author. It first hits the following url:
http://api.foxnews.com/v2/person?site=fox-news&role=personality&rows=300&callback=foo
This will return all available authors from foxnews and input them as object into a MongoDB.

It will then crawl the personal sites of each author and get the lastest articles by him/her.

Step 1: spider crwal fox_people

Step 2: execute main.py , it will iniate a CrawlerRunner

Used:
- MongoDB
- Spider Pipeline
- CrawlerRunner
- Json
