# import VADER Sentiment Analysis Packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initializing the method
analyzer = SentimentIntensityAnalyzer()

'''
Finds the general sentiment of a particular set of tweets fetched from the twitter API
# Set up counters for sentiment of tweet set
# Adopting sentiment score from Gabrovšek et al (2016) and adding a Laplace correction
# Note that sentiment score can range from -1 to 1
'''
def generalSentiment(tweetObj:dict)->float:
    arrayTweets = tweetObj["data"]
    
    numPositive, numNegative, numNeutral = 0, 0, 0

    for tweet in arrayTweets:
        sentiment = analyzer.polarity_scores(tweet["text"])["compound"]
        if (sentiment >= 0.05):
            numPositive += 1
        elif (-0.05 <= sentiment <= 0.05):
            numNeutral += 1
        else:
            numNegative += 1
        
    sentimentScore = (numPositive - numNegative) / (numPositive + numNeutral + numNegative + 3)
    return sentimentScore
