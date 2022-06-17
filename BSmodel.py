import numpy as np
from scipy.stats import norm as normal
from scipy.special import ndtr


# BlackScholes: Uses the Black-Scholes formula to provide a fair price for a European option (i.e. cannot be 
#   exercised until expiry)
def BlackScholes(timeToExp:float,stockPrice:float,strikePrice:float,riskFreeIntrest:float,volatility:float,typeOfOption:str="C")->float:
    # Calculating d1 and d2 to be used in actual Black-Scholes formula:
    
    d1 = (np.log(stockPrice/strikePrice) + (riskFreeIntrest + volatility**2/2)*timeToExp) / (volatility*np.sqrt(timeToExp))
    d2 = d1 - volatility*np.sqrt(timeToExp)

    # Plugging in d1 and d2 into Black-Scholes (note the different formulas for calls and puts):
    if (typeOfOption=="C"):
        optionPrice = stockPrice*ndtr(d1) - strikePrice * np.e **(-riskFreeIntrest*timeToExp) * ndtr(d2)
    elif (typeOfOption=="P"):
        optionPrice = strikePrice * np.e **(-riskFreeIntrest*timeToExp) * ndtr(-d2) - stockPrice*ndtr(-d1)
    else:
        print("Error, invalid option type provided!")
        return -1

    return optionPrice

# Vega: Produces a measure of an options sensitivity to implied volatility
#   (essentially the derivative of options price w.r.t. implied volatility)
#   Note that Vega is irrespective of the type of option
def vega(timeToExp:float,stockPrice:float,strikePrice:float,riskFreeIntrest:float,volatility:float)->float:
    d1 = (np.log(stockPrice/strikePrice) + (riskFreeIntrest + volatility**2/2)*timeToExp) / (volatility*np.sqrt(timeToExp))
    d2 = d1 - volatility*np.sqrt(timeToExp)

    vega = stockPrice * normal._pdf(d1) * np.sqrt(timeToExp) * 0.01
    return vega


# estimateVolatility: Uses the Newton-Raphson method to estimate volatility of an option given the current market price
#   for that option
def estimateVolatility(error:float,timeToExp:float,stockPrice:float,strikePrice:float,riskFreeIntrest:float,optionPrice:float,typeOfOption:str="C")->float:
    # We start with an initial guess of Implied Volatility derived by Brenner and Subrahmanyam (1988)
    impliedVol = np.sqrt(2*np.pi / timeToExp) * optionPrice/strikePrice

    # Define the maximum number of iterations to avoid infinite loops
    MAXiter = 500

    for i in range(MAXiter):
        # Apply BS model to current estimate of implied Vol and check if it is within the threshold
        priceGivenCurrVol = BlackScholes(timeToExp,stockPrice,strikePrice,riskFreeIntrest,impliedVol,typeOfOption)
        if (np.abs(priceGivenCurrVol-optionPrice)<=error):
            return impliedVol

        # Newton's method
        else:
            vegaVal = vega(timeToExp,stockPrice,strikePrice,riskFreeIntrest,impliedVol)*100
            impliedVol -= (priceGivenCurrVol-optionPrice)/vegaVal

    return impliedVol # Even if program did not achieve desired error, return best estimate
