'''
Assignment 1, Problem 2 -- derive the sentiment of each tweet

Created on May 6, 2013

@author: aparkin
'''
import sys
import json


def load_base_sentiment_data(sentiment_file):
    '''
    Given a file containing sentiment data in the form:
    
    word\tscore
    
    returns a dictionary mapping words to their sentiment score
    '''
    sentiment_values = {}
    with open(sentiment_file) as fobj:
        for line in fobj:
            tokens = line.strip().split('\t')
            sentiment_values[tokens[0]] = int(tokens[1])
            
    return sentiment_values


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
                tweets.append(data['text'].decode('utf-8'))
            except Exception as e:
                tweets.append("")
    return tweets


def get_sentiments_for_tweets(tweets, sentiments):
    '''
    Given a list of tweets, and a collection of sentiment scores, return a list
    of tuples mapping each tweet to its total sentiment score
    '''
    result = []
    for tweet in tweets:
        words = tweet.split()
        total = 0
        for word in words:
            total += sentiments.get(word, 0)
        result.append((tweet, total))
    return result


def dump_results(tweet_sentiments):
    '''
    Print the results of a call to get_sentiments_for_tweets() to STDOUT
    '''
    for (_, sentiment) in tweet_sentiments:
        print("%s" % (sentiment))


def process_args():
    '''
    Process the command line arguments into a dictionary, or calls show_help()
    if arguments are malformed
    '''
    if len(sys.argv) < 3:
        show_help()
        
    result = {}
    result['sentiment_file'] = sys.argv[1]
    result['tweet_file'] = sys.argv[2]
    return result


def show_help():
    ''' Display help screen & exit '''
    print("Usage is %s <sentiment_file> <tweet_file>" % sys.argv[0])
    sys.exit()


def main():
    args = process_args()
    sentiments = load_base_sentiment_data(args['sentiment_file'])
    tweets = read_tweets_from_file(args['tweet_file'])
    print("Got %s tweets" % len(tweets))
    tweet_sentiments = get_sentiments_for_tweets(tweets, sentiments)
    dump_results(tweet_sentiments)

    
if __name__ == '__main__':
    main()
