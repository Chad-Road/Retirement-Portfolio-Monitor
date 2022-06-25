import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from datetime import date
from sklearn.linear_model import LinearRegression

sns.set_style("darkgrid")
sns.set_theme("talk")

now = date.today().year
year_list = list(range(int(now), int(now) + 31))

# Vanguard index
# VTSAX = yf.Ticker("vtsax")
# vtsax_hist = VTSAX.history()
# print(vtsax_hist.head())

# Schwab index
# swtsx = yf.Ticker("swtsx")
# swtsx_hist = swtsx.history()
# print(swtsx_hist.head())

# Russell 3000 ETF
iwv = yf.download("iwv", period="max", interval='1mo')
print(iwv.index)
# iwv_hist = iwv.history()
# iwv_hist["dates"] = pd.to_datetime(iwv_hist.index)
# print(iwv_hist.groupby(iwv_hist["dates"].dt.year)["Close"].mean())

# # Wilshire 500 index
# WFIVX = 



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