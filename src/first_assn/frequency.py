'''
Assignment 1, Problem 4 -- compute term frequency 

Created on May 6, 2013

@author: aparkin
'''

import sys
import json




def read_tweets_from_file(tweet_file):
    '''
    Given a file containing raw JSON as returned by the Twitter API, returns
    a list of extracted tweets
    '''
    with open(tweet_file) as fobj:
        data = json.load(fobj)
        tweets = [tweet['text'].encode('utf-8') for tweet in data['results']]
    return tweets



def dump_results(tweet_sentiments):
    '''
    Print the results of a call to get_sentiments_for_tweets() to STDOUT
    '''
    for (tweet, sentiment) in tweet_sentiments:
        print("<%s:%s>" % (tweet, sentiment))


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


def main():
    args = process_args()
    tweets = read_tweets_from_file(args['tweet_file'])
    dump_results(tweets)

    
if __name__ == '__main__':
    main()