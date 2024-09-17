import yfinance as yf
import matplotlib.pyplot as plt

## We define the inital paramters of the strategy. The inital amount of investment. We also have a look on how many shares we get

n = 10000  
investment = n  
shares = 0  


# Download the data of Apple with yahoo finance 

data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')


# Calculs SMA50 and SMA200

data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()


# Create the rule of buying and selling 

data['Signal'] = 0
data['Signal'][50:] = [1 if data['Close'][i] > data['SMA50'][i] else 0 for i in range(50, len(data))]
data['Position'] = data['Signal'].diff()


## Portfolio value 

data['Portfolio Value'] = 0

# Simuler l'achat et la vente d'actions
for i in range(len(data)):
    if data['Position'][i] == 1:  ## Buying 
        shares = investment // data['Close'][i]  # as much as possible 
        investment -= shares * data['Close'][i]  # remaining liquidity 
        
    elif data['Position'][i] == -1 and shares > 0:  # Selling 
        investment += shares * data['Close'][i]  # all the action
        shares = 0  
    
    # Calcul de la valeur du portefeuille à chaque jour
    data['Portfolio Value'][i] = investment + shares * data['Close'][i]


# Visualiser la performance du portefeuille
plt.figure(figsize=(12,6))
plt.plot(data['Portfolio Value'], label='Portfolio Value')
plt.title('Investment Strategy -- APPL')
plt.xlabel('Date')
plt.ylabel('Value ($)')
plt.legend()
plt.show()