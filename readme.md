# Twitter Sentiment to Volatility Trade Recommender

### What is it?

This is a sentiment-based model that generates trades on European style options using their implied volatility. It uses historical volatility and sentiment data to predict current implied volatility. The model prices the option accordingly and makes suggestions based on the current price of the option. This is an extension to my "Black Scholes Equation and Formula for Options Pricing: Application of Exponential Brownian Motion and Ito’s Calculus" Project in R, which can be accessed in this repository too.

### "Black Scholes Equation and Formula for Options Pricing: Application of Exponential Brownian Motion and Ito’s Calculus" Project Report

This is a project report I prepared for MATH-365: Stochastic Process course at Amherst College under the guidance of Professor Leise. I went over summarizing the concepts of Ito's Calculus, Brownian motion and ultimately how that leads to Black Scholes model in an applied manner. At the end, I try to walk through an example application of Black Scholes numerically along with using the NASDAQ's API to get Stock Ticker data in R for volatility analysis as an extension of what things we might be interested in further analyzing. The "Twitter Sentiment to Volatility Trader Recommender" mentioned in this repository serves as an extension to this paper which I wrote.

### Usage of Twitter API & VADER Sentiment Analysis

Twitter API v2 was used to gather the top 100 tweets of a specific option. The trades were pulled from 8 a.m - to 5 p.m. EST and subsequently analyzed using the [VADER sentiment analysis tool](https://github.com/cjhutto/vaderSentiment), which is particularly suited for social media posts. The overall sentiment of the tweet was found as a weighted average, applying Laplace smoothing to correct for potentially small datasets. 

### Implied Volatility & Black-Scholes Application

The app uses the Black-Scholes model to derive the implied volatility of various option contracts of the same underlying asset. Note that this model DOES NOT account for options that can be exercised before expiry (American Options) and therefore only is effective for European style options (mostly index funds). Since it is difficult to solve for implied volatility from the differential equation directly, the model uses the Newton-Raphson method to approximate within a given error (0.0001 by default).

### Resources that were helpful and served as references:

A Sentiment Analysis Approach to the Prediction of Market Volatility - https://arxiv.org/pdf/2012.05906.pdf

Strategies for Trading Volatility With Options - https://www.investopedia.com/articles/investing/021716/strategies-trading-volatility-options-nflx.asp

Twitter sentiment around the Earnings Announcement events - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173151

Python Implementational Reference from Dhyey Mehta's VoliTrader.

R. Almgrem. Financial derivatives and partial differential equations. The American Mathematical Monthly, 109(1):1-12, 2002.

F. Black and M. Scholes. The pricing of options and corporate liabilities. The Journal of Political Economy, 81(3):637-654, 1073.8

I. Gikhman and A. Skorokhod. Introduction to the Theory of Random Processes. W. B. Saunders Company, 1969.

K. Ito. On stochastic differntial equations. Memoirs, American Mathematical Society, (4):1-51, 1951.

A. Malliaris. Ito’s calculus in financial decision making. SIAM Review, 25(4):481-496, 1983.

Gregory F. Lawler. Stochastic Calculus: An Introduction with Applications, 2014.

Panayotis Mertikopoulos. Stochastic Perturbations in Game Theory and Applications to Networks. National and Kapodistrian University of Athens. 2010.

Gregory F. Lawler. Introduction to Stochastic Processes, Second Edition, 2006.


