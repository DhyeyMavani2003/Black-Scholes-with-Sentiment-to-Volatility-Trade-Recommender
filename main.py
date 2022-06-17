from BSmodel import BlackScholes, estimateVolatility
from twitter import getTweets
from sentimentAnalysis import generalSentiment
from options import getOptionInfo
from sentimentToVol import sentimentToVol

riskFreeIntrestRate = 0.05

# Generates an investment strategy based on the ticker provided
def generateTradingStrategy(indexTicker:str):
    optionData = getOptionInfo(indexTicker)
    
    # Get implied volatility given current market conditions
    impliedVol = estimateVolatility(0.0001,
                                    optionData["timetoExp"],
                                    optionData["assetPrice"],
                                    optionData["strikePrice"],
                                    riskFreeIntrestRate,
                                    optionData["optionPrice"],
                                    optionData["typeOption"])
    
    # Get estimate of option price given by sentiment analysis
    optionSentiment = generalSentiment(getTweets("SPX","2022-01-10T13:00:01","2022-01-10T22:00:01",100))
    estimatedVol = sentimentToVol(optionSentiment)
    optionPrice = BlackScholes( optionData["timetoExp"],
                                optionData["assetPrice"],
                                optionData["strikePrice"],
                                riskFreeIntrestRate,
                                estimatedVol,
                                optionData["typeOption"])

    print(f"Current Value of option {optionData['contractSymbol']}: {optionData['optionPrice']}")
    print(f"Value of option given sentiment analysis: {optionPrice}")

    print("Recommendation: ")

    if (optionPrice>optionData['optionPrice']):
        print(f"Buy {optionData['contractSymbol']} until price of option is {optionPrice}")
    else:
        print(f"Short {optionData['contractSymbol']} until option price is {optionPrice}")

generateTradingStrategy("SPX")