# portfolio_optimizer.py

import numpy as np
import scipy.optimize as sco


def portfolio_performance(weights, mean_returns, cov_matrix):
    portfolio_return = np.sum(mean_returns * weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_volatility


# Minimum Volatility Portfolio
def portfolio_volatility(weights, mean_returns, cov_matrix):
    return portfolio_performance(weights, mean_returns, cov_matrix)[1]


def optimize_portfolio(mean_returns, cov_matrix):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    bounds = tuple((0, 1) for asset in range(num_assets))
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights must sum to 1
    initial_weights = num_assets * [1. / num_assets]

    result = sco.minimize(portfolio_volatility, initial_weights, args=args, method='SLSQP', bounds=bounds,
                          constraints=constraints)
    return result


# Risk Parity Portfolio
def calculate_risk_contributions(weights, cov_matrix):
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    marginal_contributions = np.dot(cov_matrix, weights) / portfolio_volatility
    risk_contributions = weights * marginal_contributions
    return risk_contributions


def risk_parity_objective(weights, cov_matrix):
    risk_contributions = calculate_risk_contributions(weights, cov_matrix)
    risk_contribution_diffs = np.sum((risk_contributions - np.mean(risk_contributions)) ** 2)
    return risk_contribution_diffs


def optimize_risk_parity(cov_matrix):
    num_assets = len(cov_matrix)
    initial_weights = np.array(num_assets * [1. / num_assets])
    bounds = tuple((0, 1) for _ in range(num_assets))
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights must sum to 1

    result = sco.minimize(risk_parity_objective, initial_weights, args=(cov_matrix,), method='SLSQP', bounds=bounds,
                          constraints=constraints)
    return result


# Mean-Variance Optimization (Max Sharpe Ratio)
def sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.03):
    portfolio_return, portfolio_volatility = portfolio_performance(weights, mean_returns, cov_matrix)
    return (portfolio_return - risk_free_rate) / portfolio_volatility


def optimize_mean_variance(mean_returns, cov_matrix, risk_free_rate=0.03):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)
    bounds = tuple((0, 1) for asset in range(num_assets))
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights must sum to 1
    initial_weights = num_assets * [1. / num_assets]

    result = sco.minimize(lambda x: -sharpe_ratio(x, mean_returns, cov_matrix, risk_free_rate), initial_weights,
                          method='SLSQP', bounds=bounds, constraints=constraints)
    return result


# Efficient Frontier Calculation
def efficient_frontier(mean_returns, cov_matrix, num_portfolios=100):
    results = np.zeros((3, num_portfolios))
    weights_record = []

    num_assets = len(mean_returns)
    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_return, portfolio_volatility = portfolio_performance(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = results[0, i] / results[1, i]  # Sharpe ratio

    return results[0], results[1]
