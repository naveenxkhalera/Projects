import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Fetch stock data for a BSE-listed company (e.g., TATA Motors - TATAMOTORS.BO)
stock_data = yf.download("TATAMOTORS.BO", start="2010-01-01", end="2025-01-01")

# Display the first few rows
print(stock_data.head())

# Plot Closing Price Trend
plt.figure(figsize=(10,6))
plt.plot(stock_data['Close'], label='TATA Motors Close Price')
plt.title('TATA Motors Stock Price Trend (BSE)')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.show()

# Calculate Moving Averages (50-day and 200-day)
stock_data['50_Day_MA'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_Day_MA'] = stock_data['Close'].rolling(window=200).mean()

# Plot stock price with moving averages
plt.figure(figsize=(10,6))
plt.plot(stock_data['Close'], label='TATA Motors Close Price')
plt.plot(stock_data['50_Day_MA'], label='50-Day Moving Average', linestyle='--')
plt.plot(stock_data['200_Day_MA'], label='200-Day Moving Average', linestyle='--')
plt.title('TATA Motors Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.show()

# Calculate Daily Returns and 30-Day Volatility
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data['30_Day_Volatility'] = stock_data['Daily_Return'].rolling(window=30).std()

# Plot 30-Day Volatility
plt.figure(figsize=(10,6))
plt.plot(stock_data['30_Day_Volatility'], label='30-Day Volatility')
plt.title('TATA Motors Stock Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# Prepare data for Linear Regression (predict closing price)
stock_data['Date_Ordinal'] = stock_data.index.map(lambda x: x.toordinal())
X = stock_data[['Date_Ordinal']]  # Feature: Date in ordinal format
y = stock_data['Close']  # Target: Close price

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')
