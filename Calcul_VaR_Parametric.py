import numpy as np 
import yfinance as yf 
from datetime import date, timedelta
import scipy.stats as stats



endDate = date.today()
years = 4
StartDate = endDate - timedelta(365*years)

ticker = 'AAPL'

stock = yf.download(ticker, StartDate, endDate)

value = stock['Adj Close']

returns = np.diff(value) / value[:-1]

mean_returns = np.mean(returns)
std_returns = np.std(returns)

confidence_level = 0.95
z_score = stats.norm.ppf(confidence_level)

VaR = mean_returns - z_score*std_returns

print(VaR)

## Backtesting

VaRbreach = 0 
for a in returns: 
    if a < VaR :
        VaRbreach = VaRbreach + 1
    else :
        VaRbreach = VaRbreach
    
