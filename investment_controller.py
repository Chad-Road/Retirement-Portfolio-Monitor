import pandas as pd
import investment_model
from os.path import exists

# TODO add method to caclulate taxes on investment

class InvestmentMenu:
    """ Discription """

    def __init__(self, investment_df):
        self.investment_df = pd.read_csv(investment_df)

    # current report and suggestions
    def portfolio_eval(self):
        # portfolio return 
        # portfolio volatility
        pass

    # import investments
    def import_investment(self):
        print("Warning! this will close current investments and open new file")
        import_choice = input("Press Y to continue or any other key to cancel").upper()
        if import_choice == "Y":
            import_path = input("Please enter file path to your saved CSV file")
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

    # add investments
    def add_investment(self):
        choice = input("Do you know the average return and variance of the investment you want to add? Y/N ").upper()
        if choice == "Y":
            initial_value = input("What is the initial USD($) value of your investment?: ")
            mean_return = input("What is the average annual return of your investment?: ")
            return_risk = input("What is the varaibility percentage for its annual return?: ")


    # delete investments
    def del_investment(self):
        pass


    # preview possible investment
    def preview_new_investment(self):
        pass


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
            elif choice == "0":
                print("Exiting program")
                break
            else:
                print("Error")

