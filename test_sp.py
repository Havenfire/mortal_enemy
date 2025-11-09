import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the investment parameters
investment_amount = 10  # Amount invested each Thursday
start_date = datetime(2020, 3, 11)  # Three years ago from today
end_date = datetime(2023, 3, 11)  # Today

# Fetch historical S&P 500 data
ticker = '^GSPC'  # S&P 500 index symbol
sp500_data = yf.download(ticker, start=start_date, end=end_date)

# Choose the appropriate price column: use 'Adj Close' if available, else fall back to 'Close'
price_column = 'Adj Close' if 'Adj Close' in sp500_data.columns else 'Close'

# Filter data to include only Thursdays
sp500_data['Date'] = sp500_data.index
sp500_data['Weekday'] = sp500_data['Date'].dt.weekday
thursdays = sp500_data[sp500_data['Weekday'] == 3]  # 3 corresponds to Thursday

total_invested = len(thursdays) * investment_amount
print("Total $ Invested:", total_invested)

# Initialize variables to track total shares purchased
total_shares = 0

# Simulate investments on each Thursday
for date, row in thursdays.iterrows():
    close_price = row[price_column]
    shares_purchased = investment_amount / close_price
    total_shares += shares_purchased

# Get the latest price as a scalar
latest_price = sp500_data[price_column].iloc[-1]
total_value = total_shares * latest_price

print(f"Total value of the investment as of {end_date.date()}: ${total_value:.2f}")
print("Total Gain:", total_value - total_invested)
print("Percentage Gain:", (total_value - total_invested) / total_invested * 100)
