# Import required libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical stock data (e.g., Apple Inc.)
ticker = "AAPL"
data = yf.download(ticker, start="2022-01-01", end="2023-01-01")

# Step 2: Calculate moving averages
short_window = 20  # 20-day moving average
long_window = 50   # 50-day moving average

data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
data['Long_MA'] = data['Close'].rolling(window=long_window).mean()

# Step 3: Generate trading signals
data['Signal'] = 0
data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1  # Buy signal
data.loc[data['Short_MA'] < data['Long_MA'], 'Signal'] = -1 # Sell signal

# Step 4: Create positions based on signal changes
data['Position'] = data['Signal'].diff()

# Step 5: Calculate strategy returns
data['Market_Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Market_Returns'] * data['Signal'].shift(1)

# Step 6: Calculate cumulative returns
data['Cumulative_Market_Returns'] = (1 + data['Market_Returns']).cumprod() - 1
data['Cumulative_Strategy_Returns'] = (1 + data['Strategy_Returns']).cumprod() - 1

# Step 7: Plot the stock price and buy/sell signals
plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['Short_MA'], label='20-Day MA', alpha=0.9)
plt.plot(data['Long_MA'], label='50-Day MA', alpha=0.9)

# Plot buy signals
buy_signals = data[data['Position'] == 2]  # Signal changed from -1 to 1 (buy)
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal', s=100)

# Plot sell signals
sell_signals = data[data['Position'] == -2]  # Signal changed from 1 to -1 (sell)
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal', s=100)

plt.title(f'Moving Average Crossover Strategy for {ticker}')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Step 8: Print performance summary
total_strategy_return = data['Cumulative_Strategy_Returns'][-1] * 100
total_market_return = data['Cumulative_Market_Returns'][-1] * 100
print(f"Total Strategy Return: {total_strategy_return:.2f}%")
print(f"Total Market Return: {total_market_return:.2f}%")
