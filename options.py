# importing Yahoo Finance, Pandas and datetime packages
import yfinance as yf
import pandas as pd
from datetime import datetime

'''
Returns relevant information on various options using yahoo finance
# Makes API call
# Fetching options data
# Info of option + underlying security
# Out of the money options
# Since close to the money options are more sensitive to implied volatility changes, the algorithm selects an option with a strike price close to current market price
'''
def getOptionInfo(ticker:str,typeOption:str="C")->dict:
    
    stock = yf.Ticker("^"+ticker) # ^ added for indexes
    info = stock.info
    options_exp = stock.options[2] # Arbitrarily takes third availible expiry date
    
    optionsChain = stock.option_chain(options_exp)
    if (typeOption=="C"):
        data = optionsChain[0]
    else:
        data = optionsChain[1]
        
    assetPrice = info["regularMarketPrice"]
    timetoExp = ((datetime.strptime(options_exp, r"%Y-%m-%d") - datetime.today()).days) / 365
    
    OutTM = data[data["inTheMoney"]==False]

    option = OutTM.iloc[[2]]

    strikePrice = option.iloc[0]["strike"]
    optionPrice = (option.iloc[0]["ask"] + option.iloc[0]["bid"])/2
    contractSymbol = option.iloc[0]["contractSymbol"]

    toReturn = {"contractSymbol":contractSymbol,
                "assetPrice":assetPrice,
                "optionPrice":optionPrice,
                "strikePrice":strikePrice,
                "timetoExp":timetoExp,
                "typeOption":typeOption}
    
    return toReturn
