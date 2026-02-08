# ML Portfolio Optimization - Magnificent Seven Version

## Project Overview
This is a **modified and extended version** of the original "Stock Portfolio Machine Learning Optimization" project.

**Original Project** (by Professor / Hunter Gould):  
https://github.com/kendrickl1675/ML-Portfolio-Optimization  
- Focuses on portfolio optimization using Mean-Variance, Machine Learning predictions, and Black-Litterman model.  
- Original creation date: 11/29/2023  
- Author: Hunter Gould

**This Fork/Modified Version** (by Jacky)  
- Forked and cloned from my friend's repository[](https://github.com/kendrickl1675/ML-Portfolio-Optimization), which was based on the professor's version.  
- Major changes:  
  - Replaced the original 10-stock portfolio with the **Magnificent Seven** (AAPL, MSFT, NVDA, GOOGL, AMZN, META, TSLA)  
  - Adjusted `max_volatility` from 0.225 to 0.35–0.40 to accommodate higher volatility of tech stocks  
  - Tested different ML models (Linear Regression → attempting Random Forest)  
  - Updated market cap estimates in `black_litterman_model.py` for more realistic Black-Litterman adjustments  
  - Fixed minor bugs (e.g., swapped stats box labels, handled empty filtered_results in MV optimization)  
  - Backtested performance from ~2021 to 2026, with observations on why pure MV sometimes outperforms ML+BL in this period  

This version is created for learning and course assignment purposes.

## Features (Inherited + Modified)
- Mean-Variance Optimization with weight constraints  
- Machine Learning strategies for generating investor views (Linear Regression / Random Forest)  
- Black-Litterman model to incorporate ML predictions  
- Portfolio performance metrics (Sharpe, Sortino, Information Ratio)  
- Comparative cumulative returns visualization


## Installation
To use the Portfolio Analysis Suite, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/jackyka19/Algo-Electornic-Project-ML-Portfolio.git
   ```
2. Navigate to the repository's directory
   ```bash
   cd ML-Portfolio-Optimization
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Recommended) Use the provided Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate MLBL
   ```

## Usage
Run the main script:
   ```bash
   python main.py
   ```

Current focus: Magnificent Seven stocks optimization.

You can easily change the portfolio in main.py and black_litterman_model.py to test other stock sets.

## Sample Output
Below is an example of the output produced by running the code with sample input parameters. The table shows the allocation percentages for each stock in the original Mean-Variance Optimization, as well as the Machine Learning-enhanced Mean-Variance Optimization. The Chart shows the performance of the three portfolios against the market representation (SPY) and provices metrics for each portfolio's performance.

```plaintext
      Original MV Optimization ML MV Optimization
AAPL    17.86%          16.11%             31.17%
MSFT    16.67%          24.96%             43.12%
NVDA    15.48%           2.03%             12.98%
GOOGL   14.29%           4.06%              2.41%
AMZN    13.10%           1.60%              3.92%
META    11.90%          23.76%              3.16%
TSLA    10.71%          27.49%              3.23%
```

![Example Output](https://github.com/Gouldh/ML-Portfolio-Optimization/blob/main/test_Figure_1.png) 

## License
This project is open-sourced under the MIT License. For more information, please refer to the `LICENSE` file.

**Author**: Hunter Gould         
**Date**: 11/29/2023
