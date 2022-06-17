# VoliTrader

### What is it?

VoliTrader is a sentiment-based model that generates trades on European style options using their implied volatility. It uses historical volatility and sentiment data to predict current implied volatility. The model prices the option accordingly and makes suggestions based on the current price of the option. 

### Twitter + Sentiment Analysis

Twitter API v2 was used to gather the top 100 tweets of a specific option. The trades were pulled from 8 a.m - to 5 p.m. EST and subsequently analyzed using the [VADER sentiment analysis tool](https://github.com/cjhutto/vaderSentiment), which is particularly suited for social media posts. The overall sentiment of the tweet was found as a weighted average, applying LaPlace smoothing to correct for potentially small datasets. 

### Implied Volatility & Black-Scholes

The app uses the Black-Scholes model to derive the implied volatility of various option contracts of the same underlying asset. Note that this model DOES NOT account for options that can be exercised before expiry (American Options) and therefore only is effective for European style options (mostly index funds). Since it is difficult to solve for implied volatility from the differential equation directly, the model uses the Newton-Raphson method to approximate within a given error (0.0001 by default).

### Disclaimer

VoliTrader is proof of concept. Any output from the program should be taken for informational purposes only, and should be exercised at your own risk. Conduct your own research before using this model.

### Resources that were helpful:

A Sentiment Analysis Approach to the Prediction of Market Volatility - https://arxiv.org/pdf/2012.05906.pdf

 Strategies for Trading Volatility With Options - https://www.investopedia.com/articles/investing/021716/strategies-trading-volatility-options-nflx.asp

Twitter sentiment around the Earnings Announcement events - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173151