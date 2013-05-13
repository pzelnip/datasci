'''
Assignment 1, Problem 3 -- derive the sentiment of unseen words

Created on May 6, 2013

@author: aparkin
'''
import sys
import json
from itertools import groupby
from operator import itemgetter


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
                # Gross, must just swallow the exception
                pass
    return tweets


def get_basic_sentiment_for_tweet(tweet, sentiments):
    '''
    Given a single tweet, generates the base sentiment score & returns a list
    of words not seen, along with the base sentiment score for this tweet
    '''
    words = tweet.split()
    total = 0
    unknown_words = []
    for word in words:
        wordscore = sentiments.get(word, None)
        if wordscore is None:
            unknown_words.append(word)
        else:
            total += wordscore
    return [(word, total) for word in unknown_words]


def score_unknown_word(scores):
    '''
    Scores the unknown word using the heuristic of the sum of the sentiment
    scores for each tweet the word appears in, divided by the number of 
    occurences of the word
    '''
    sumscore = sum(scores) * 1.0
    count = len(scores) * 1.0
    return sumscore / count


def get_sentiments_for_tweets(tweets, sentiments):
    '''
    Given a list of tweets, and a collection of sentiment scores, return a list
    of tuples mapping each tweet to its total sentiment score
    '''
    result = []
    scores = []
    for tweet in tweets:
        scores.extend(get_basic_sentiment_for_tweet(tweet, sentiments))
        
    for word, group in groupby(scores, itemgetter(0)):
        newscore = score_unknown_word([score for _, score in group])
        result.append((word, newscore))
        
    return result


def dump_results(scores):
    '''
    Print the results to STDOUT
    '''
    for (word, score) in scores.iteritems():
        print("%s %s" % (word, score))


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
    tweet_sentiments = dict(get_sentiments_for_tweets(tweets, sentiments))
    dump_results(tweet_sentiments)

    
if __name__ == '__main__':
    main()
