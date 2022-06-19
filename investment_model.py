import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
from sklearn.linear_model import LinearRegression




class Investment:
    """ General class of investments """

    def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees):
        self.name = name
        self.initial_value = initial_value 
        self.mean_return = mean_return
        self.return_risk = return_risk
        self.expected_tax = expected_tax
        self.liquidity_penalty = liquidity_penalty
        self.other_fees = other_fees

    def add_inv(self):
        pass

    def get_stock_info(self):
        # 
        pass


class EquityBased(Investment):
    """ Sub-class of equity based investments including stocks, funds, and ETFs """

    def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees, num_shares):
        super().__init__(name, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees)
        self.num_shares = num_shares


class MaturationBased(Investment):
    """ Sub-class of maturation based investments including bonds, IRAs, and 401ks """

    def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees,  maturation_time, early_penalty):
        super().__init__(name, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees)
        self.maturation_time = maturation_time
        self.early_penalty = early_penalty

    def add_ma_inv(self):
        pass


class PortfolioEvaluation:
    """ pass """

    # portfolio mean return
        # use market base rate return
        # use historical return

    # portfolio volatility
        # use market base rate volitility
        # use historical volatility

    # sharpe ratio
        # (asset mean return - risk free return rate) / (std of portfolio)

    # portfolio autocorrelation

    pass

class InvestmentVisualization:
    def __init__(self):
        pass

    # historical averages projection
        # stock market
        # bonds
        # 


def calculate_mean_return():
    pass

def calculate_return_variability():
    pass

def calculate_investment_tax():
    pass