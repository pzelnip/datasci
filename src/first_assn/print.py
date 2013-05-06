'''
The first "intro" assignment for the Data Science class, prints out Tweets for
the first 10 pages on a Twitter query for "microsoft"

Created on May 6, 2013

@author: aparkin
'''
import json
import urllib


FEED_URL="http://search.twitter.com/search.json"


def retrieve(url, num_pages=10):
    for page_num in range(1, num_pages + 1):
        values = {"q" : "microsoft", "page" : page_num}
        data = json.load(urllib.urlopen(url, urllib.urlencode(values)))
        
        print("===========================Tweets for page %s===========================" % page_num)
        for tweet in data[u'results']:
            print(tweet[u'text'].encode('utf-8'))
        

def main():
    retrieve(FEED_URL, 5)


if __name__ == "__main__":
    main()
