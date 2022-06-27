from cProfile import label
import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from datetime import date
from sklearn.linear_model import LinearRegression

# TODO use random sampling to create interval prediction animation

# Real Return of S&P (also Tbills, Tbonds, and Real Estate)
sandp = pd.read_csv("GitHub\\Retirement-Portfolio-Monitor\\datasets\\sp_return.csv")

# Historical return of Schwab and Vanguard total market funds
index_returns = pd.read_csv("GitHub\\Retirement-Portfolio-Monitor\\datasets\\index_returns.csv")

# Set preferred Seaborn styles
sns.set("notebook", style="darkgrid", rc={"lines.linewidth": 4})


def get_mean_index_return():
    """ Get mean combined return of Schwab and Vanguard total market funds """
    
    global index_returns
    index_returns_mean = index_returns["Combined Index Return"].mean()
    return index_returns_mean


def get_mean_index_std():
    """ Get the standard deviation of the combinded return of Schwab and Vanguard total market funds """

    global index_returns
    index_returns_std = index_returns["Combined Index Return"].std()
    return index_returns_std


def get_mean_historical_return():

    global sandp
    sandp_real_return = sandp["S&P 500 Real Return"].mean()
    return sandp_real_return


def get_mean_real_estate_return():

    global sandp
    mean_real_estate = sandp["Real Estate Real Return"].mean()
    return mean_real_estate


def get_ten_yr_tbond():

    global sandp
    ten_year_bond = sandp['10Year TBond Real Return'].mean()
    return ten_year_bond


def get_current_index_returns():
    """ Get annual mean and standard deviation of return of Schwab and Vanguard funds
    
    Note: Vanguard world fund left out due to higher variability
    and lower return, but could be included as a market centered
    way to increase diversification.
    """

    # Schwab Total Market Index
    swtsx = yf.download("swtsx", peroid="max", interval="1mo")
    swtsx_mean = swtsx.groupby(swtsx.index.year).mean()
    swtsx_std = swtsx.groupby(swtsx.index.year).std()

    # Vanguard Total Market Index
    vti = yf.download("vti", peroid="max", interval="1mo")
    vti_mean = vti.groupby(vti.index.year).mean()
    vti_std = vti.groupby(vti.index.year).std()

    # Vanguard World Index Fund (excluding U.S.)
    # Generally more volatile and lower return than US market
    # veu = yf.download("veu", peroid="max", interval="1mo")
    # veu_mean = veu.groupby(veu.index.year).mean()
    # veu_std = veu.groupby(veu.index.year).std()


def display_historical_market(amount=1000):
    
    global sandp

    now = date.today().year
    year_list = list(range(int(now), int(now) + 31))
    

    sandp_real_return = sandp["S&P 500 Real Return"].mean()
    sandp_130_percent = sandp_real_return * 1.3
    sandp_120_percent = sandp_real_return * 1.2
    sandp_110_percent = sandp_real_return * 1.1
    sandp_90_percent = sandp_real_return * .9
    sandp_80_percent = sandp_real_return * .8
    sandp_70_percent = sandp_real_return * .7

    sandp_130_list = []
    sandp_120_list = []
    sandp_110_list = []
    sandp_mean_list = []
    sandp_90_list = []
    sandp_80_list = []
    sandp_70_list = []

    for i, x in enumerate(range(31)):
            if i == 0:
                temp = amount
                sandp_mean_list.append(temp)
                sandp_70_list.append(temp)
                sandp_80_list.append(temp)
                sandp_90_list.append(temp)
                sandp_110_list.append(temp)
                sandp_120_list.append(temp)
                sandp_130_list.append(temp)
            else:
                temp = sandp_mean_list[i-1] * (1 + sandp_real_return)
                temp1 = sandp_70_list[i-1] * (1 + sandp_70_percent)
                temp2 = sandp_80_list[i-1] * (1 + sandp_80_percent)
                temp3 = sandp_90_list[i-1] * (1 + sandp_90_percent)
                temp4 = sandp_110_list[i-1] * (1 + sandp_110_percent)
                temp5 = sandp_120_list[i-1] * (1 + sandp_120_percent)
                temp6 = sandp_130_list[i-1] * (1 + sandp_130_percent)

                sandp_mean_list.append(temp)
                sandp_70_list.append(temp1)
                sandp_80_list.append(temp2)
                sandp_90_list.append(temp3)
                sandp_110_list.append(temp4)
                sandp_120_list.append(temp5)
                sandp_130_list.append(temp6)

    ax = sns.lineplot(x=year_list, y=sandp_mean_list, label="Mean Return")
    ax.fill_between(year_list, sandp_mean_list, sandp_110_list, facecolor="blue", alpha=0.2, label="10% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_90_list, facecolor="blue", alpha=0.2)
    ax.fill_between(year_list, sandp_mean_list, sandp_120_list, facecolor="blue", alpha=0.15, label="20% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_80_list, facecolor="blue", alpha=0.15)
    ax.fill_between(year_list, sandp_mean_list, sandp_130_list, facecolor="blue", alpha=0.1, label="30% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_70_list, facecolor="blue", alpha=0.1)

    plt.suptitle("Projected 30 Year Return")
    ax.set(title="Using Historic Inflation Adjusted Return of S&P 500", xlabel="Years", ylabel="Dollars USD")
    plt.legend(loc="upper left")

    plt.show()

#display_historical_market()


def display_mean_index_market(amount=1000.0):

    global index_returns

    now = date.today().year
    year_list = list(range(int(now), int(now) + 31))

    index_returns_mean = index_returns["Combined Index Return"].mean()
    index_130_percent = index_returns_mean * 1.3
    index_120_percent = index_returns_mean * 1.2
    index_110_percent = index_returns_mean * 1.1
    index_70_percent = index_returns_mean * .7
    index_80_percent = index_returns_mean * .8
    index_90_percent = index_returns_mean * .9

    index_130_list = []
    index_120_list = []
    index_110_list = []
    index_mean_list = []
    index_90_list = []
    index_80_list = []
    index_70_list = []

    for i, x in enumerate(range(31)):
            if i == 0:
                temp = amount
                index_mean_list.append(temp)
                index_70_list.append(temp)
                index_80_list.append(temp)
                index_90_list.append(temp)
                index_110_list.append(temp)
                index_120_list.append(temp)
                index_130_list.append(temp)
            else:
                temp = index_mean_list[i-1] * (1 + index_returns_mean)
                temp1 = index_70_list[i-1] * (1 + index_70_percent)
                temp2 = index_80_list[i-1] * (1 + index_80_percent)
                temp3 = index_90_list[i-1] * (1 + index_90_percent)
                temp4 = index_110_list[i-1] * (1 + index_110_percent)
                temp5 = index_120_list[i-1] * (1 + index_120_percent)
                temp6 = index_130_list[i-1] * (1 + index_130_percent)

                index_mean_list.append(temp)
                index_70_list.append(temp1)
                index_80_list.append(temp2)
                index_90_list.append(temp3)
                index_110_list.append(temp4)
                index_120_list.append(temp5)
                index_130_list.append(temp6)

    ax = sns.lineplot(x=year_list, y=index_mean_list, label="Mean Index Fund Return")
    ax.fill_between(year_list, index_mean_list, index_110_list, facecolor="blue", alpha=0.2, label="10% above/below normal return")
    ax.fill_between(year_list, index_mean_list, index_90_list, facecolor="blue", alpha=0.2)
    ax.fill_between(year_list, index_mean_list, index_120_list, facecolor="blue", alpha=0.15, label="20% above/below normal return")
    ax.fill_between(year_list, index_mean_list, index_80_list, facecolor="blue", alpha=0.15)
    ax.fill_between(year_list, index_mean_list, index_130_list, facecolor="blue", alpha=0.1, label="30% above/below normal return")
    ax.fill_between(year_list, index_mean_list, index_70_list, facecolor="blue", alpha=0.1)
    
    plt.suptitle("Projected 30 Year Return")
    ax.set(title="Using Historic Returns of Schwab and Vanguard Total Market Funds", xlabel="Years", ylabel="Dollars USD")
    plt.legend(loc="upper left")
    
    plt.show()

# display_mean_index_market()

def display_mean_real_estate(amount=1000):
    global sandp

    now = date.today().year
    year_list = list(range(int(now), int(now) + 31))
    

    sandp_real_return = sandp["Real Estate Real Return"].mean()
    sandp_130_percent = sandp_real_return * 1.3
    sandp_120_percent = sandp_real_return * 1.2
    sandp_110_percent = sandp_real_return * 1.1
    sandp_90_percent = sandp_real_return * .9
    sandp_80_percent = sandp_real_return * .8
    sandp_70_percent = sandp_real_return * .7

    sandp_130_list = []
    sandp_120_list = []
    sandp_110_list = []
    sandp_mean_list = []
    sandp_90_list = []
    sandp_80_list = []
    sandp_70_list = []

    for i, x in enumerate(range(31)):
            if i == 0:
                temp = amount
                sandp_mean_list.append(temp)
                sandp_70_list.append(temp)
                sandp_80_list.append(temp)
                sandp_90_list.append(temp)
                sandp_110_list.append(temp)
                sandp_120_list.append(temp)
                sandp_130_list.append(temp)
            else:
                temp = sandp_mean_list[i-1] * (1 + sandp_real_return)
                temp1 = sandp_70_list[i-1] * (1 + sandp_70_percent)
                temp2 = sandp_80_list[i-1] * (1 + sandp_80_percent)
                temp3 = sandp_90_list[i-1] * (1 + sandp_90_percent)
                temp4 = sandp_110_list[i-1] * (1 + sandp_110_percent)
                temp5 = sandp_120_list[i-1] * (1 + sandp_120_percent)
                temp6 = sandp_130_list[i-1] * (1 + sandp_130_percent)

                sandp_mean_list.append(temp)
                sandp_70_list.append(temp1)
                sandp_80_list.append(temp2)
                sandp_90_list.append(temp3)
                sandp_110_list.append(temp4)
                sandp_120_list.append(temp5)
                sandp_130_list.append(temp6)

    ax = sns.lineplot(x=year_list, y=sandp_mean_list, label="Inflation Adjusted Returns")
    ax.fill_between(year_list, sandp_mean_list, sandp_110_list, facecolor="blue", alpha=0.2, label="10% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_90_list, facecolor="blue", alpha=0.2)
    ax.fill_between(year_list, sandp_mean_list, sandp_120_list, facecolor="blue", alpha=0.15, label="20% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_80_list, facecolor="blue", alpha=0.15)
    ax.fill_between(year_list, sandp_mean_list, sandp_130_list, facecolor="blue", alpha=0.1, label="30% above/below normal return")
    ax.fill_between(year_list, sandp_mean_list, sandp_70_list, facecolor="blue", alpha=0.1)

    plt.suptitle("Projected 30 Year Return")
    ax.set(title="Using Historic Inflation Adjusted Real Estate Returns", xlabel="Years", ylabel="Dollars USD")
    plt.legend(loc="upper left")

    plt.show()

display_mean_real_estate()


def display_ten_year_tbond(amount=1000):
    global sandp

    now = date.today().year
    year_list = list(range(int(now), int(now) + 31))
    
    sandp_real_return = sandp["10Year TBond Real Return"].mean()
 
    sandp_mean_list = []
    for i, x in enumerate(range(31)):
            if i == 0:
                temp = amount
                sandp_mean_list.append(temp)
            else:
                temp = sandp_mean_list[i-1] * (1 + sandp_real_return)
                sandp_mean_list.append(temp)
  

    ax = sns.lineplot(x=year_list, y=sandp_mean_list, label="Mean Return of 10 Year TBond")
    plt.suptitle("Projected 30 Year Return")
    ax.set(title="Using Historic Return of 10 Year TBond", xlabel="Years", ylabel="Dollars USD")
    plt.legend(loc="upper left")

    plt.show()

# display_ten_year_tbond()

def display_portfolio_projection(percent_stocks, percent_bonds, percent_real_estate):
    
    bond_return = get_ten_yr_tbond()
    market_return = get_mean_historical_return()
    estate_return = get_mean_real_estate_return()
    bond_weight = percent_bonds
    market_weight = percent_stocks
    estate_weight = percent_real_estate

    portfolio_return = (bond_return * bond_weight) + (market_return * market_weight) + (estate_return * estate_weight)



def display_indv_investment_history(symbol):
    
    ticker_history = yf.Ticker(symbol)
    ticker_history.history(period="max", interval="1mo")

def display_ticker_report(symbol):
    
    ticker_report = yf.Ticker(symbol)
    ticker_info = ticker_report.info
    bus_sum = ticker_info["longBusinessSummary"]
    sector = ticker_info["sector"]
    industry = ticker_info["industry"]
    total_assets = ticker_info["totalAssets"]
    five_year_div_yield = ticker_info["fiveYearAvgDividendYield"]
    five_year_return = ticker_info["fiveYearAverageReturn"]
    short_name = ticker_info["shortName"]
    comapny_symbol = ticker_info["symbol"]
    trailing_pe = ticker_info["trailingPE"]
    short_ratio = ticker_info["shortRatio"]
    nav_price = ticker_info["navPrice"]
    market_price = ticker_info["regularMarketPrice"]

    
    print(f"Business Summary: {bus_sum}")
    print(f"Sector: {sector}")
    ######################



if __name__=="__main__":
    pass