# **Risk-Based Asset Allocation Strategy for Portfolio Optimization**

## **Project Overview**
This project focuses on building a portfolio optimization model using various risk-based asset allocation strategies on a set of Indian stocks. The model optimizes portfolio weights using three primary techniques: 
- **Minimum Volatility**
- **Risk Parity**
- **Mean-Variance Optimization (Sharpe Ratio)**

By leveraging Python libraries such as NumPy, SciPy, and Matplotlib, we analyze the risk-return profiles of these strategies, offering tailored solutions for different investor risk preferences.

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**: 
  - NumPy
  - SciPy
  - Matplotlib

## **Indian Stocks Used in the Portfolio**
The project focuses on a portfolio of five major Indian stocks:
1. **Tata Consultancy Services (TCS)**
2. **Infosys (INFY)**
3. **HDFC Bank (HDFCBANK)**
4. **Reliance Industries (RELIANCE)**
5. **ICICI Bank (ICICIBANK)**

## **Optimization Techniques Implemented**
1. **Minimum Volatility Strategy**: Focuses on minimizing the portfolio's overall risk (volatility) while achieving a reasonable return.
2. **Risk Parity Strategy**: Balances the risk contribution from each stock by equally distributing risk among all portfolio assets.
3. **Mean-Variance Optimization (Sharpe Ratio)**: Maximizes the portfolio's risk-adjusted return, giving preference to stocks that offer the best trade-off between risk and return.

## **Portfolio Insights**
- **Minimum Volatility Portfolio**: 
  - **Weights**: `[0.2405, 0.3828, 0.0066, 0.0703, 0.2998]`
  - **Expected Daily Return**: 0.0604%
  - **Daily Volatility**: 1.2025%
  
- **Risk Parity Portfolio**: 
  - **Weights**: `[0.2, 0.2, 0.2, 0.2, 0.2]`
  - **Expected Daily Return**: 0.0719%
  - **Daily Volatility**: 1.2640%
  
- **Mean-Variance Portfolio (Sharpe Ratio)**: 
  - **Weights**: `[0.0, 0.0, 0.0, 1.0, 0.0]` (All weight allocated to HDFC Bank)
  - **Expected Daily Return**: 0.0840%
  - **Daily Volatility**: 1.9653%

## **What I Learned and Implemented**
1. **Analyzed** the risk-return profiles of five major Indian stocks.
2. **Developed** a portfolio optimization model implementing three different strategies: Minimum Volatility, Risk Parity, and Mean-Variance.
3. **Optimized portfolio weights** based on volatility, correlation, and risk parity principles.
4. **Implemented visualizations** to showcase portfolio performance and comparison of the three strategies.
5. **Gained insights** into how different strategies suit varying investor risk appetites, ranging from conservative (low-risk, stable returns) to aggressive (high-risk, high-return) investors.

## **Key Numbers and Results**
- **Stocks Analyzed**: 5 major Indian stocks (TCS, INFY, HDFCBANK, RELIANCE, ICICIBANK).
- **Optimization Techniques**: 3 strategies implemented (Minimum Volatility, Risk Parity, Mean-Variance Optimization).
- **Data Used**: Daily stock price data for Indian stocks (can be sourced from Yahoo Finance or other market data APIs).
- **Visualization**: Comparative analysis using risk-return trade-offs plotted using Matplotlib.

## **Conclusion**
This project demonstrates how different optimization techniques can be applied to build portfolios tailored to different risk-return profiles. The Mean-Variance strategy offers higher returns at higher risk, while the Minimum Volatility strategy minimizes risk for more conservative investors. The Risk Parity strategy provides balanced risk exposure, ensuring a well-diversified portfolio.
