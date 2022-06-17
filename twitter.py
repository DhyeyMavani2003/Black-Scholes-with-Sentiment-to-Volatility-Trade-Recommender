import requests
from sentimentAnalysis import generalSentiment
from twitterAuth import headers

# getTweets: Uses twitter's api to get tweets referencing a stock symbol
#   Note that startTime and endTime must be formatted according to ISO 8601 (YYYY-MM-DDTHH:mm:ss UTC)
def getTweets(ticker:str,startTime:str,endTime:str,numofEntries:int)->dict:
    url = (f'https://api.twitter.com/2/tweets/search/recent?query={ticker}'
                                                        f'&start_time={startTime}Z'
                                                        f'&end_time={endTime}Z'
                                                        f'&max_results={numofEntries}'
                                                        f'&tweet.fields=public_metrics')
    result = requests.get(url,headers=headers)
    return result.json()
 