'''
Assignment 1, Problem 4 -- compute term frequency 

Created on May 6, 2013

@author: aparkin
'''

import sys
import json
from collections import Counter


def read_tweets_from_file(tweet_file):
    '''
    Given a file containing raw JSON as returned by the Twitter API, returns
    a list of extracted tweets
    '''
    tweets = []
    with open(tweet_file) as fobj:
        for line in fobj:
            try:
                data = json.loads(line)
                tweets.append(data['text'].encode('utf-8'))
            except Exception as e:
                # Gross, must just swallow the exception
                pass
    return tweets


def dump_results(frequencies):
    '''
    Print the results of a call to get_sentiments_for_tweets() to STDOUT
    '''
    for (term, frequency) in frequencies.iteritems():
        print("%s %s" % (term, frequency))


def process_args():
    '''
    Process the command line arguments into a dictionary, or calls show_help()
    if arguments are malformed
    '''
    if len(sys.argv) < 2:
        show_help()
        
    result = {}
    result['tweet_file'] = sys.argv[1]
    return result


def show_help():
    ''' Display help screen & exit '''
    print("Usage is %s <tweet_file>" % sys.argv[0])
    sys.exit()


def process_tweets(tweets):
    terms = []
    for tweet in tweets:
        terms.extend(tweet.split())
    
    return {word : (float(count) / len(terms)) for word, count in Counter(terms).iteritems()}


def main():
    args = process_args()
    tweets = read_tweets_from_file(args['tweet_file'])
    result = process_tweets(tweets)
    dump_results(result)

    
if __name__ == '__main__':
    main()