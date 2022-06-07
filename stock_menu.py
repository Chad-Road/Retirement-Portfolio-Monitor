from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Traditional, Robo
import matplotlib.pyplot as plt
import yfinance as yf
import csv
import os


def add_stock(stock_list):
    # Add new stocks to your stock list
    option = ""
    while option != "0":
        print("Stock to be added")
        stock_symbol = input("Enter the three letter stock symbol: ").upper()
        stock_name = input("Enter the stock name: ")
        num_shares = float(input("Enter the number of shares you want to purchase: "))
        new_stock = Stock(stock_symbol, stock_name, num_shares)
        stock_list.append(new_stock)
        option = input("Press 1 to enter a new stock or 0 to quit: ")

def delete_stock(stock_list):
    # Delete stocks from your stock list
    print("Which stock would you like to delete? ")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]", end=" ")
    stock_to_del = input("Enter the stock symbol you want to delete: ").upper()
    found = False
    count = 0
    for stock in stock_list:
        if stock.symbol == stock_to_del:
            found = True
            stock_list.pop(count)
        count += 1
    if found == True:
        print("Deleted", stock_to_del)
    else:
        print("Stock not found in stock list")
    input("Press Enter to continue ***1")

    
# List stocks being tracked
def list_stocks(stock_list):
    print("STOCK LIST ----- ")
    print("SYMBOL      NAME     SHARES")
    print("==============================")
    for stock in stock_list:
        print(f"{stock.symbol}    {stock.name}    {stock.shares}")
    input("Press Enter to Continue ***")
    
    # Add Daily Stock Data
def add_stock_data(stock_list):
    print("Add Daily Stock Data ---- ")
    print("Stock LIst: [", end=" ")
    for stock in stock_list:
       print(stock.symbol, end=" ")
    print("]")
    symbol = input("which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do not use Spaces")
        print("Enter a Blank line to Quite")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
            print("Data Entry Complete")
        else:
            print("Symbol not found *** ")
            input("Press Enter to Continue ***")


def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(company)
    plt.show()


# Display Chart
def display_chart(stock_list):
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, " ", end=" ")
    print("]", end="")
    symbol = input("Please input the stock symbol: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, symbol)
    else:
        print("Stock symbol not found")
    input("Press enter to continue")
                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("Goodbye")

def main():
    stock_list = []
    main_menu(stock_list)

if __name__ == "__main__":
    main()