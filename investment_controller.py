
import pandas as pd
import investment_model
from os.path import exists

# TODO add method to caclulate taxes on investment

class InvestmentMenu:
    """ Discription """

    def __init__(self, investment_file="investment.csv"):
        """ Basic command line menu and functions to create and load investments
        
        Args:
        investment_file (pandas DataFrame): [Dataframe of investments]

        
        """
        
        column_names = ["Name", "Symbol", "Initial Value", "Mean Return", "Return Risk", "Tax", "Other Fees", 
                            "Annual Dividends", "Price Per Share", "Number of Shares", "Coupon Rate", 
                            "Maturation Time", "Early Penalty"]
        
        if exists("investment.csv"):
            self.investment_df = pd.read_csv("investments.csv")
        else:
            self.investment_df = pd.DataFrame(columns=column_names)

            

        

    # current report and suggestions
    def portfolio_eval(self):
        # portfolio return 
        # portfolio volatility
        pass

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
        # TODO write to file after every new investment is added

        export_name = input("What would you like to name your export file?: ")
        self.investment_df.to_csv(export_name)

    def save_file(self):
        self.investment_df.to_csv("investment.csv")

    # add investments
    def add_investment(self):
        equity_or_bond = input("Is the investment (1)equity based (e.g. stock) or (2)maturation based (e.g. bond)?: 1/2 ").upper()

        if equity_or_bond == "1":
            print("========== Investment Input ==========")
            stock_name = input("What is the name of the stock?: ") 
            symbol_or_code = input("What is the stock symbol, ticker symbol, fund code, etc.?: ")
            price_per_share = float(input("What is the current price per share?: "))
            num_shares = float(input("How many shares are you purchasing?: "))
            expect_tax = float(input("What is the expected tax on the investment?: "))
            other_fees = float(input("Are there any other expected fees?: "))

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
            print(f"Other fees connected to this investment are: {other_fees}")
            is_correct = input("Is the above information correct?: Y/N").upper()
            if is_correct == "Y":
                new_inv = {'symbol': symbol_or_code, 'Initial Value': initial_value, 'Mean Return': mean_return,
                            'Tax': expect_tax, 'Other Fees': other_fees, 'Price Per Share': price_per_share,
                            'Number of Shares': num_shares, }
                self.investment_df.append(new_inv)
            elif is_correct == "N":
                input("Press enter to return to main menu")
            else:
                input("Press enter to return to main menu")
                
        elif equity_or_bond == "2":
            pass
        else:
            print("Please choose a correct option?: ")
        
        
# #["Name", "Symbol", "Initial Value", "Mean Return", "Return Risk", "Tax", "Other Fees", 
#                         "Annual Dividends", "Price Per Share", "Number of Shares", "Coupon Rate", 
#                         "Maturation Time", "Early Penalty"]


    # delete investments
    def del_investment(self):
        pass


    # preview possible investment
    def preview_new_investment(self):
        pass

    def user_menu(self):
        user_choice = input("Do you want to create a (1)new user or switch to another (2)existing user: ")
        if user_choice == "1":
            user_name = input("What would you like the new username to be?: ")
            years_to_retire = input("How many years until this new user retires?: ")
            risk = input("On a scale of 1-5, 1 being no risk, 5 being very high risk, how risky do you want this user's investments to be: ")
            tax_bracket = input("What is this user's approximate annual income to determine approximate tax costs?: ")
            
            print("Is the following information correct?")
            print(f"The new user's username is: {user_name}")
            print(f"The approximate number of years until retirement is: {years_to_retire}")
            print(f"The level of risk this user is comfortable with is: {risk}")
            print(f"The approximate annual income of this user for tax calculations is: {tax_bracket}")

            user_correct = input("Is this user information correct?: Y/N").upper()

            if user_correct == "Y":
                self.user = investment_model.User(user_name, tax_bracket, years_to_retire, risk)


    def cmd_line_menu(self):
        choice = ""
        while True:
            print("Investments Menu")
            print("1: Report and Suggestions")
            print("2: Import other investments")
            print("3: Export investments")
            print("4: Add investments")
            print("5: Delete investmetns")
            print("6: Preview possible investment")
            print("7: User menu")
            print("0: Exit program")
            choice = input("Please enter your choice: ")

            if choice == "1":
                self.portfolio_eval(self.investment_df)
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
            elif choice == "7":
                self.user_menu()
            elif choice == "0":
                self.save_file()
                print("Exiting program")
                break
            else:
                print("Error")

if __name__== "__main__":
    investments = InvestmentMenu()
    investments.cmd_line_menu()