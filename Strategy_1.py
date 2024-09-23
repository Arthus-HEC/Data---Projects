import yfinance as yf
import matplotlib.pyplot as plt

n = 10000  
investment = n  
shares = 0  

data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')

data['SMA50'] = data['Close'].rolling(window=50).mean()

data['Signal'] = 0
data['Signal'][50:] = [1 if data['Close'][i] > data['SMA50'][i] else 0 for i in range(50, len(data))]
data['Position'] = data['Signal'].diff()

data['Portfolio Value'] = 0

for i in range(len(data)):
    if data['Position'][i] == 1:  
        shares = investment // data['Close'][i]  
        investment -= shares * data['Close'][i]  
        
    elif data['Position'][i] == -1 and shares > 0:  
        investment += shares * data['Close'][i]  
        shares = 0  
    
    
    data['Portfolio Value'][i] = investment + shares * data['Close'][i]



plt.figure(figsize=(12,6))
plt.plot(data['Portfolio Value'], label='Portfolio Value')
plt.title('Investment Strategy -- APPL')
plt.xlabel('Date')
plt.ylabel('Value ($)')
plt.legend()
plt.show()
