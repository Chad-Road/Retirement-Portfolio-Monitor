from stock_class import Stock

# Stocks, Bonds, Mutual Funds, CDs
# Type, 

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

class Investment:
    """ General class of investments including stock based, bond, and retirement"""

    def __init__(self, value, mean_return, return_risk):
        self.value = value 
        self.mean_return = mean_return
        self.return_risk = return_risk

class StockBased(Investment):
    def __init__(self):
        pass


class MaturationBased(Investment):
    def __init__(self):
        pass

if __name__ == "__main__":
    pass
