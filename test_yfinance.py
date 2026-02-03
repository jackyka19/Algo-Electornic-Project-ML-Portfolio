import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta

portfolio = {
    'AAPL': 1500.0,  # Apple Inc.
    'JNJ': 1200.0,   # Johnson & Johnson
    'PG': 800.0,     # Procter & Gamble Co.
    'JPM': 1300.0,   # JPMorgan Chase & Co.
    'XOM': 700.0,    # Exxon Mobil Corporation
    'MMM': 600.0,    # 3M Company
    'SO': 500.0,     # Southern Company
    'VZ': 600.0,     # Verizon Communications Inc.
    'NKE': 1000.0,   # NIKE, Inc.
    'DD': 800.0      # DuPont de Nemours, Inc.
}

ticker = list(portfolio.keys())
today = date.today()
current_date = today.strftime("%Y-%m-%d")

# Define dates for training and backtesting
training_start_date = today - relativedelta(years=10)
training_end_date = today - relativedelta(years=5)
backtesting_start_date = training_end_date
backtesting_end_date = current_date

data = yf.download(ticker, start=training_start_date, end=training_end_date, progress=False)
print(data.columns)

