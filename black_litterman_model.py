import numpy as np


def black_litterman_adjustment(market_returns, investor_views, view_confidences, historical_data, tau=0.025):
    """
    Adjust market returns based on the investor's views and confidences using historical data
    :param dict market_returns: expected market returns for each asset
    :param dict investor_views: investor's specific views on the expected returns of assets
    :param dict view_confidences: investor's confidence in each view
    :param pandas Dataframe historical_data: historical market data
    :param float tau: The uncertainty of the market equilibrium
    :return: numpy array, the adjusted returns for each asset after considering the investor's views
    """
    num_assets = len(market_returns)
    P = np.eye(num_assets)  # Proportion matrix
    Q = np.array(list(investor_views.values())).reshape(-1, 1)

    cov_matrix = historical_data['Close'].pct_change().dropna().cov()

    # Ensure investor views and confidences are also arrays
    omega = np.diag([tau / confidence for confidence in view_confidences.values()])

    # Black-Litterman formula
    inv_omega = np.linalg.inv(omega)
    adjusted_returns = np.linalg.inv(np.linalg.inv(tau * cov_matrix) + np.dot(P.T, np.dot(inv_omega, P)))
    adjusted_returns = np.dot(adjusted_returns, np.dot(np.linalg.inv(tau * cov_matrix), np.array(list(market_returns.values())).reshape(-1, 1)) + np.dot(P.T, np.dot(inv_omega, Q)))

    return adjusted_returns.flatten()


# def get_market_caps(tickers):
#     """
#     Provides example market capitalizations for a predefined set of stocks. TEMPORARILY USING PLACEHOLDER DATA
#     :param tickers: list of tickers
#     :return: A dictionary with tickers and their example market capitalizations.
#     """
#     market_caps = {
#         'AAPL': 2.0e12,  # Apple Inc.
#         'JNJ': 800.0e9,  # Johnson & Johnson
#         'PG': 400.0e9,   # Procter & Gamble Co.
#         'JPM': 250.0e9,  # JPMorgan Chase & Co.
#         'XOM': 200.0e9,  # Exxon Mobil Corporation
#         'MMM': 230.0e9,  # 3M Company
#         'SO': 220.0e9,   # Southern Company
#         'VZ': 260.0e9,   # Verizon Communications Inc.
#         'NKE': 400.0e9,  # NIKE, Inc.
#         'DD': 130.0e9    # DuPont de Nemours, Inc.
#     }
#     return market_caps

def get_market_caps(tickers):
    """
    Provides approximate market capitalizations for the Magnificent Seven stocks.
    Values are rough estimates as of early 2026 (in trillions USD).
    These are placeholders — for real projects, fetch real-time data.
    """
    market_caps = {
        'AAPL':  3.5e12,   # Apple ≈ 3.5 trillion
        'MSFT':  3.2e12,   # Microsoft ≈ 3.2 trillion
        'NVDA':  3.0e12,   # NVIDIA ≈ 3.0 trillion (very volatile)
        'GOOGL': 2.1e12,   # Alphabet (Google) ≈ 2.1 trillion
        'AMZN':  2.0e12,   # Amazon ≈ 2.0 trillion
        'META':  1.5e12,   # Meta ≈ 1.5 trillion
        'TSLA':  1.2e12,   # Tesla ≈ 1.2 trillion
    }
    
    # 只返回目前 portfolio 裡有的股票市值
    return {ticker: market_caps.get(ticker, 1.0e12) for ticker in tickers}


def get_market_returns(market_caps, index_return):
    """
    Calculate market returns based on market capitalizations and index return.
    :param dict market_caps: Market capitalizations of the stocks.
    :param float index_return: Return of the market index.
    :return: A dictionary with tickers and their market returns.
    """
    total_market_cap = sum(market_caps.values())
    return {ticker: (cap / total_market_cap) * index_return for ticker, cap in market_caps.items()}
