import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

stock_name = 'AAPL'
end_date = datetime.today()
start_date = end_date - timedelta(days = 365)

stock_data = yf.download(
    stock_name, 
    start = start_date, 
    end = end_date)

d_returns = stock_data['Adj Close'].pct_change(1)
stock_vol = d_returns.std()

stock_price = stock_data['Adj Close'][-1]
strike_price = stock_price # At the money

risk_free_rate = 0.05
maturity = 1

def european_option_price(S0, K, v, r, T, nSim, flag):
    z = np.random.standard_normal(nSim)
    S_fwd = S0 * np.exp((r-0.5* v**2)*T + v*np.sqrt(T)*z)
    
    if flag == 'call':
        payoff = np.maximum(S_fwd - K, 0)
    elif flag == 'put':
        payoff = np.maximum(K-S_fwd, 0)
    else :
        print("incorrect flag")
        return 
    
    return np.exp(-r*T)*np.sum(payoff)/nSim

nSim = 100000
option_price = european_option_price(
    stock_price, strike_price, stock_vol, risk_free_rate, maturity, nSim, 'put')

    

