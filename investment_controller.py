import pandas as pd
import investment_model
from os.path import exists

# ===================== Notes and To-Do ===================== #

# TODO add method to caclulate taxes on investment
# TODO write to file after every new investment is added
# TODO estimate taxes based on capital gains and income tax bracket

# ==================== Investment Menu Class ==================== #

class InvestmentMenu:
    """ Creates a commmand line menu to manipulate and analyze real and historic investments """

    def __init__(self, investment_file="investment.csv"):
        """ Basic command line menu and functions to create and load investments
        
        Args:
        investment_file (pandas DataFrame): [Dataframe of investments]        
        """

        # Default column names for DataFrame
        column_names = ["Name", "Symbol", "Type", "Initial Value", "Mean Return", "Return Risk", 
                        "Annual Dividends", "Price Per Share", "Number of Shares", 
                        "Coupon Rate", "Maturation Time", "Face Value"]
        

        # Check if file exits and create file if no file exits
        if exists("investment.csv"):
            self.investment_df = pd.read_csv("investments.csv")
        else:
            self.investment_df = pd.DataFrame(columns=column_names)


# ==================== Main Menu ==================== #

    def cmd_line_menu(self):
        """ Main menu for accessing all basic functions """

        choice = ""
        while True:
            print("")
            print("Investments Menu")
            print("1: Report and Suggestions")
            print("2: Import other investments")
            print("3: Export investments")
            print("4: Add investments")
            print("5: Delete investmetns")
            print("6: Preview possible investment")
            print("0: Exit program")
            choice = input("Please enter your choice: ")

            if choice == "1":
                self.portfolio_eval_menu()
            elif choice == "2":
                self.import_investment()
            elif choice == "3":
                self.export_investment()
            elif choice == "4":
                self.add_investment()
            elif choice == "5":
                self.del_investment()
            elif choice == "6":
                self.preview_new_investment()
            elif choice == "0":
                self.save_file()
                print("Exiting program")
                break
            else:
                print("Error")

# ===================== Portfolio Evaluation Submenu =================== #

    # current report and suggestions
    def portfolio_eval_menu(self):
        """ Portfolio evaluation and historic investment visualizations """

        print("")
        print("======== Reports and Suggestions Menu ========")
        print("----- Projected Returns Visualizations -----")
        print("1: Portfolio Report and Suggestions")
        print("2: Display My Portfolio 30 Year Projected Return")
        print("3: Display Recent Index Fund 30 Year Projected Return")
        print("4: Display S&P 500 30 Year Projected Return")
        print("5: Display 10 Year Treasury Bond 30 Year Projected Return")
        print("6: Display Real Estate 30 Year Projected Return")
        print("----- Ticker Reports and Histories -----")
        print("7: Get Ticker Report")
        print("8: Get Ticker Price History")

        choice = input("Please choose a menu option or press any other key to return to main menu: ")

        if choice == "1":
            investment_model.portfolio_report_sugggestions()
        elif choice == "2":
            investment_model.display_portfolio_projection()
        elif choice == "3":
            investment_model.display_mean_index_market()
        elif choice == "4":
            investment_model.display_historical_market()
        elif choice == "5":
            investment_model.display_ten_year_tbond()
        elif choice == "6":
            investment_model.display_mean_real_estate()
        elif choice == "7":
            self.ticker_report()
        elif choice == "8":
            self.ticker_history()
        else:
            input("Please hit enter to return to main menu")


    def portfolio_report(self):
        investment_model.portfolio_report_sugggestions()

    def my_portfolio_projections(self):
        investment_model.display_portfolio_projection()

    def index_projection(self):
        investment_model.display_mean_index_market()

    def sandp_projection(self):
        investment_model.display_historical_market()

    def bond_projection(self):
        investment_model.display_ten_year_tbond()

    def real_estate_projection(self):
        investment_model.display_mean_real_estate()

    def ticker_report(self):
        symbol = input("Please enter ticker symbol: ")
        print(f"Retrieving data for {symbol}")
        print("Please wait...")
        try:
            ticker_dict = investment_model.display_ticker_report(symbol)
            print("")
            print("========== Ticker Report ==========")
            print(f"Ticker Symbol: {ticker_dict['symbol']}")
            print(f"Business Name: {ticker_dict['short_name']}")
            print(f"Industry: {ticker_dict['industry']}")
            print(f"Business Summary: {ticker_dict['bus_sum']}")
            print("----------------------------------------")
            print(f"Total Assets: {ticker_dict['total_assets']}")
            print(f"Five Year Return: {ticker_dict['five_year_return']}")
            print(f"Five Year Dividend Yield: {ticker_dict['five_year_div_yield']}")
            print(f"Market Price: {ticker_dict['market_price']}")
            print(f"Net Asset Value: {ticker_dict['nav_price']}")
            print(f"Trailing PE: {ticker_dict['trailing_pe']}")
            print(f"Asset Beta: {ticker_dict['beta']}")
  
        except:
            print("Error: No ticker symbol found")

    def ticker_history(self):
        symbol = input("Please enter ticker symbol: ")
        print(f"Retrieving five year quarterly data for {symbol}")
        print("Please wait...")
        try:
            investment_history = investment_model.display_indv_investment_history(symbol)
            pd.set_option("display.max_rows", None)
            print(investment_history)

        except:
            print("Error: No ticker symbol found")

# ========================= Main Menu Functions ========================= #


    # import investments
    def import_investment(self):
        print("Warning! this will close current investments and open new file")
        import_choice = input("Press Y to continue or any other key to cancel ").upper()
        if import_choice == "Y":
            import_path = input("Please enter file path to your saved CSV file ")
            if exists(import_path):
                new_inv = InvestmentMenu(import_path)
                new_inv.cmd_line_menu()
            else:
                print("Incorrect path")
        input("Press enter to return to main menu")


    # export investments
    def export_investment(self):

        export_name = input("What would you like to name your export file?: ")
        self.investment_df.to_csv(export_name)

    def save_file(self):
        self.investment_df.to_csv("investment.csv")

    # add investments
    def add_investment(self):
        equity_or_bond = input("""Is the investment (1) equity based (e.g. stock), (2) maturation based 
                                (e.g. bond)?, or (3) real estate: 1/2 """).upper()

        if equity_or_bond == "1":
            print("========== Investment Input ==========")
            stock_name = input("What is the name of the stock?: ") 
            symbol_or_code = input("What is the stock symbol, ticker symbol, fund code, etc.?: ")
            price_per_share = float(input("What is the current price per share?: "))
            num_shares = float(input("How many shares are you purchasing?: "))


            initial_value = price_per_share * num_shares
            mean_return = investment_model.get_mean_return()
            return_risk = investment_model.get_return_variability()
            annual_dividends = investment_model.get_dividends()

            print("========== Investment Information ==========")
            print(f"The name of the investment is: {stock_name}")
            print(f"The symbol or ticker code is: {symbol_or_code}")
            print(f"The current price per share is: {price_per_share}")
            print(f"The number of shares that you are buying is: {num_shares}")
            print(f"The average return on this investment is: {mean_return}")
            is_correct = input("Is the above information correct?: Y/N").upper()
            if is_correct == "Y":
                new_inv = {'symbol': symbol_or_code, 'Initial Value': initial_value, 'Mean Return': mean_return, 
                            'Price Per Share': price_per_share,'Number of Shares': num_shares, }
                self.investment_df.append(new_inv, ignore_index=True)
            elif is_correct == "N":
                input("Press enter to return to main menu")
            else:
                input("Press enter to return to main menu")
                
        elif equity_or_bond == "2":
            print("========== Investment Input ==========")
            stock_name = input("What is the name or type of bond ?: ") 
            initial_bond_price = input("What is the initial bond price?: ")
            coupon_rate = float(input("What is the coupon rate of the bond?: "))
            face_value = float(input("What is the face value of the bond?: "))
            maturation_time = float(input("What is the maturation time for the bond?: "))


            print("========== Investment Information ==========")
            print(f"The name of the investment is: {stock_name}")
            print(f"The symbol or ticker code is: {symbol_or_code}")
            print(f"The current price per share is: {price_per_share}")
            print(f"The number of shares that you are buying is: {num_shares}")
            print(f"The average return on this investment is: {mean_return}")
            is_correct = input("Is the above information correct?: Y/N").upper()
            if is_correct == "Y":
                new_inv = {'symbol': symbol_or_code, 'Initial Value': initial_value, 'Mean Return': mean_return, 
                            'Price Per Share': price_per_share,'Number of Shares': num_shares, }
                self.investment_df.append(new_inv, ignore_index=True)
            elif is_correct == "N":
                input("Press enter to return to main menu")
            else:
                input("Press enter to return to main menu")
        
        elif equity_or_bond == "3":
            pass
        else:
            print("Please choose a correct option?: ")
        
        
#column_names = ["Name", "Symbol", "Type", "Initial Value", "Mean Return", "Return Risk", 
                       # "Annual Dividends", "Price Per Share", "Number of Shares", 
                       # "Coupon Rate", "Maturation Time", "Face Value"]


    # delete investments
    def del_investment(self):
        print(self.investment_df["Name"])
        index_number = input("Please enter the index number of the investment you would like to delete")
        investment_to_delete = self.investment_df.iloc[index_number]
        self.investment_df.drop(investment_to_delete, inplace=True)


    # preview possible investment
    def preview_new_investment(self):

        symbol = input("Please enter the ticker symbol for the investment you wish to visualize: ")
        
        pass

    


    

if __name__== "__main__":
    investments = InvestmentMenu()
    investments.cmd_line_menu()