'''
Assignment 1, Problem 6 -- Top 10 hashtags 

Created on May 6, 2013

@author: aparkin
'''

import sys
import json
from collections import Counter


def read_hashtags_from_file(tweet_file):
    '''
    Given a file containing raw JSON as returned by the Twitter API, returns
    a list of extracted hashtags
    '''
    tags = []
    with open(tweet_file) as fobj:
        for line in fobj:
            try:
                data = json.loads(line)
                tags.extend([tag['text'].encode('utf-8') for tag in data['entities']['hashtags']])
            except Exception as e:
                print("Error processing line: %s" % e)
            
    return tags


def dump_results(results):
    '''
    Print the results of a call to get_sentiments_for_tweets() to STDOUT
    '''
    for (term, frequency) in results:
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


def process_tags(tags):
    result = list(Counter(tags).iteritems())
    result.sort(key=lambda tup: tup[1], reverse=True)
    return result[:10]

def main():
    args = process_args()
    tags = read_hashtags_from_file(args['tweet_file'])
    result = process_tags(tags)
    dump_results(result)

    
if __name__ == '__main__':
    main()
