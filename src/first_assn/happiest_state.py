'''
Assignment 1, Problem 5 -- derive the happiest state

Created on May 7, 2013

@author: aparkin
'''
import sys
from itertools import ifilter
import operator
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
                tweets.append(data)
            except Exception as e:
                # Gross, must just swallow the exception
                pass
    return tweets


def get_state_from_full_name(name):
    return name.split(",")[-1].strip()


def tweet_of_interest(data):
    place = data.get('place', None)
    if (place is not None):
        country = place.get('country', None)
        country_code = place.get('country_code', None)
        name = place.get('full_name', None)
        if (country == u"United States" or country_code == u"US"):
            state = get_state_from_full_name(name)
            if len(state) == 2:
                return True
    return False


def print_tweet(tweet):
    s = "Country: %s  CountryCode: %s  State: %s" % (
         tweet['place']['country'],
         tweet['place']['country_code'],
         get_state_from_full_name(tweet['place']['full_name']))
    return s


def get_sentiment_for_tweet(sentiments, tweet):
    total = 0
    for word in tweet['text'].split():
        total += sentiments.get(word, 0)
    return total


def sentiments_by_state(sentiments, tweets):
    result = {}
    for tweet in tweets:
        state = get_state_from_full_name(tweet['place']['full_name'])
        sentiment = get_sentiment_for_tweet(sentiments, tweet)
        if result.has_key(state) :
            result[state] += sentiment
        else:
            result[state] = sentiment

    return result


def show_help():
    ''' Display help screen & exit '''
    print("Usage is %s <sentiment_file> <tweet_file>" % sys.argv[0])
    sys.exit()


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


def main():
    args = process_args()
    sentiments = load_base_sentiment_data(args['sentiment_file'])
    all_tweets = read_tweets_from_file(args['tweet_file'])
    tweets = ifilter(tweet_of_interest, all_tweets)
    state_sentiments = sentiments_by_state(sentiments, tweets)
    
    state, _ = sorted(state_sentiments.iteritems(), key=operator.itemgetter(1), 
                          reverse=True)[0]
    print(state)


if __name__ == "__main__":
    main()


