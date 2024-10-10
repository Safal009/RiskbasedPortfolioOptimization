# visualization.py

import matplotlib.pyplot as plt


def plot_efficient_frontier(frontier_returns, frontier_volatility, optimal_portfolio_volatility,
                            optimal_portfolio_risk_parity, optimal_portfolio_mvo):
    plt.figure(figsize=(10, 6))
    plt.scatter(frontier_volatility, frontier_returns, c='blue', marker='x', label='Efficient Frontier')
    plt.scatter(optimal_portfolio_volatility[1], optimal_portfolio_volatility[0], c='red', marker='o',
                label='Min Volatility Portfolio')
    plt.scatter(optimal_portfolio_risk_parity[1], optimal_portfolio_risk_parity[0], c='green', marker='D',
                label='Risk Parity Portfolio')
    plt.scatter(optimal_portfolio_mvo[1], optimal_portfolio_mvo[0], c='purple', marker='s',
                label='Mean-Variance Portfolio')

    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Expected Return')
    plt.title('Efficient Frontier and Optimal Portfolios')
    plt.legend()
    plt.show()
