import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from datetime import date
from sklearn.linear_model import LinearRegression

### nned total return plus total yield

# Set preferred Seaborn styles
sns.set_style("darkgrid")
sns.set_theme("talk")

now = date.today().year
year_list = list(range(int(now), int(now) + 31))

sandp = pd.read_csv("GitHub\\Retirement-Portfolio-Monitor\\datasets\\sp_return.csv")
# sandp.loc[len(sandp.index)] = ["2022"]
# print(type(sandp["Year"]))
# print(sandp.iloc[75:])

 # Schwab Total Market Index
swtsx = yf.download("swtsx", peroid="max", interval="1mo")
swtsx_mean = swtsx.groupby(swtsx.index.year).mean()
swtsx_std = swtsx.groupby(swtsx.index.year).std()

# Vanguard Total Market Index
vti = yf.download("vti", peroid="max", interval="1mo")
vti_mean = vti.groupby(vti.index.year).mean()
vti_std = vti.groupby(vti.index.year).std()

print(swtsx_mean.head())
print(vti_mean.head())


def get_total_market_return():
    """ Get annual return of two largest total market funds 
    
    Note: Vanguard world fund left out due to higher variability
    and lower return, but could be included as a market centered
    way to increase diversification.
    """

    # Real Return of S&P since 1928
    sandp = pd.read_csv("GitHub\\Retirement-Portfolio-Monitor\\datasets\\sp_return.csv")

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

    market_return = pd.merge()

    #return total_return

# tote_return = get_total_market_return()
# print(tote_return.iloc[69:])


def display_mean_market(amount=1000.0):

    mean_return = []
    low_return = []
    high_return = []
    for i, x in enumerate(range(31)):
        if i == 0:
            temp = amount
            mean_return.append(temp)
        else:
            temp = mean_return[i-1] * 1.0829
            mean_return.append(temp)

    #print(mean_return)
    ax = sns.lineplot(x=year_list, y=mean_return, ci="sd")
    plt.show()

#display_mean_market()


def display_mean_bonds():
    pass

def display_portfolio_projection():
    pass

def display_each_investment():
    pass


def get_mean_return(symbol):
    pass

def get_return_variability(symbol):
    pass

def get_dividends(symbol):
    pass

def get_investment_tax():
    pass




if __name__=="__main__":
    pass