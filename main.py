# main.py

from data_loader import load_data
from risk_metrics import calculate_metrics
from portfolio_optimizer import optimize_portfolio, optimize_risk_parity, optimize_mean_variance, efficient_frontier, portfolio_performance
from visualization import plot_efficient_frontier

# Step 1: Load data
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'HINDUNILVR.NS']
data = load_data(tickers, '2020-01-01', '2024-01-01')

# Step 2: Calculate risk metrics
returns, mean_returns, cov_matrix = calculate_metrics(data)

# Step 3: Optimize for Minimum Volatility
optimized_result_volatility = optimize_portfolio(mean_returns, cov_matrix)
optimal_weights_volatility = optimized_result_volatility['x']

# Step 4: Optimize for Risk Parity
optimized_result_risk_parity = optimize_risk_parity(cov_matrix)
optimal_weights_risk_parity = optimized_result_risk_parity['x']

# Step 5: Optimize for Mean-Variance (Sharpe Ratio)
optimized_result_mvo = optimize_mean_variance(mean_returns, cov_matrix)
optimal_weights_mvo = optimized_result_mvo['x']

# Step 6: Calculate efficient frontier
frontier_returns, frontier_volatility = efficient_frontier(mean_returns, cov_matrix)

# Step 7: Portfolio performance for each strategy
optimal_portfolio_volatility = portfolio_performance(optimal_weights_volatility, mean_returns, cov_matrix)
optimal_portfolio_risk_parity = portfolio_performance(optimal_weights_risk_parity, mean_returns, cov_matrix)
optimal_portfolio_mvo = portfolio_performance(optimal_weights_mvo, mean_returns, cov_matrix)

# Step 8: Print Results
print("Minimum Volatility Weights:", optimal_weights_volatility)
print("Risk Parity Weights:", optimal_weights_risk_parity)
print("Mean-Variance (Sharpe Ratio) Weights:", optimal_weights_mvo)

print("Portfolio Performance (Minimum Volatility):", optimal_portfolio_volatility)
print("Portfolio Performance (Risk Parity):", optimal_portfolio_risk_parity)
print("Portfolio Performance (Mean-Variance):", optimal_portfolio_mvo)

# Step 9: Plot Efficient Frontier and Optimal Portfolios
plot_efficient_frontier(frontier_returns, frontier_volatility, optimal_portfolio_volatility,
                        optimal_portfolio_risk_parity, optimal_portfolio_mvo)
