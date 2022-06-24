import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
from sklearn.linear_model import LinearRegression




class InvestmentEvaluation:
    """ pass """

    def __init__(self, investment_df):
        pass
    # overall portfolio report
        # show graph for  5 10 20 30 years
        # show risk report
        # show

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
        # mean return for market
        # mean return for bonds

        # 


def get_mean_return(symbol):
    pass

def get_return_variability(symbol):
    pass

def get_dividends(symbol):
    pass

def get_investment_tax():
    pass







# class Investment:
#     """ General class of investments """

#     def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, other_fees):
#         self.name = name
#         self.initial_value = initial_value 
#         self.mean_return = mean_return
#         self.return_risk = return_risk
#         self.expected_tax = expected_tax
#         self.other_fees = other_fees

#     def add_inv(self):
#         pass

#     def get_stock_info(self):
#         # 
#         pass


# class EquityBased(Investment):
#     """ Sub-class of equity based investments including stocks, funds, and ETFs """

#     def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, other_fees, 
#                     symbol_or_code, annual_dividend, price_per_share, num_shares):
#         super().__init__(name, initial_value, mean_return, return_risk, expected_tax, other_fees)
#         self.symbol_or_code = symbol_or_code
#         self.annual_dividend = annual_dividend
#         self.price_per_share = price_per_share
#         self.num_shares = num_shares


# class MaturationBased(Investment):
#     """ Sub-class of maturation based investments including bonds, IRAs, and 401ks """

#     def __init__(self, name, initial_value, mean_return, return_risk, expected_tax, other_fees, coupon_rate, maturation_time):
#         super().__init__(name, initial_value, mean_return, return_risk, expected_tax, other_fees)
#         self.coupon_rate = coupon_rate
#         self.maturation_time = maturation_time

#     def add_ma_inv(self):
#         pass

#     def calc_bond_ytm(self):
#         # ytm = coupon ((face value - current price)
#         pass