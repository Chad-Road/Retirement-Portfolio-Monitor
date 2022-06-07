
from stock_class import Stock

class Retirement_Account:
    def __init__(self, balance, number):
        self.balance = balance
        self.number = number

class Traditional(Retirement_Account):
    def __init__(self, balance, number):
        super().__init__(balance, number)
        self.Stock_List = []

    def add_stock(self, stock_data):
        self.Stock_List.append(stock_data)

class Robo(Retirement_Account):
    def __init__(self, balance, number, years):
        super().__init__(balance, number)
        self.years = years

    def investment_return(self):
        return (self.years * self.balance * 1.05)


# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.
def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Traditional
    stock_list =[]
    testStock = Stock("TEST", "Testcompany", 200)
    stock_list.append(testStock)
    print("Testing Add Retirement Account...",end="")
    try:
        testRetire = Retirement_Account(200,"12345")
        print("Successful!")
    except:
        print("***Adding retirement Account Failed!")
        error_count = error_count+1
        error_list.append("Retirement Constructor Error")
    print("Testing Add Traditional Account...",end="")
    try:
        testTraditional = Traditional(200,"12345")
        testTraditional.add_stock(stock_list)
        print("Successful!")
    except:
        print("***Adding Traditional Account Failed!")
        error_count = error_count+1
        error_list.append("Traditional Constructor Error")
   
    # Test Change Balance
    print("Test Change Balance...",end="")
    try:
        testTraditional.balance = 1000
        if testTraditional.balance == 1000:
            print("Successful!")
        else:
            print("***ERROR! Balance change unsuccessful.")
            error_count = error_count+1
            error_list.append("Balance Change Error")
    except:
        print("***ERROR! Balance change failed.")
        error_count = error_count+1
        error_list.append("Balance Change Failure")
        
    # Test Change Number
    print("Test Change Number...",end="")
    try:
        testTraditional.number = "99999"
        if testTraditional.number == "99999":
            print("Successful!")
        else:
            print("***ERROR! Number change unsuccessful.")
            error_count = error_count+1
            error_list.append("Number Change Error")
    except:
        print("***ERROR! Number change failed.")
        error_count = error_count+1
        error_list.append("Number Change Failure")
        
        
        
        
    print("Testing Add Robo Account...",end="")
    try:
        testRobo = Robo(200,"12345",5)
        print("Successful!")
    except:
        print("***Adding Robo Account Failed!")
        error_count = error_count+1
        error_list.append("Robo Constructor Error")
   
    # Test Change years
    print("Test Change Balance...",end="")
    try:
        testRobo.years = 1000
    
        if testRobo.years == 1000:
            print("Successful!")
        else:
            print("***ERROR! Years change unsuccessful.")
            error_count = error_count+1
            error_list.append("Years Change Error")
    except:
        print("***ERROR! Years change failed.")
        error_count = error_count+1
        error_list.append("Years Change Failure")
        
    # Test investment return
    print("Test investment return...",end="")
    try:
        testRobo.years = 1000
        testRobo.balance = 1
        if testRobo.investment_return() == 1050:
            print("Successful!")
        else:
            print("***ERROR!Investment return unsuccessful.")
            error_count = error_count+1
            error_list.append("investment return Error")
    except:
        print("***ERROR! investment return failed.")
        error_count = error_count+1
        error_list.append("Investment Return Failure") 
   
    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)
    print("Goodbye")
# Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()
