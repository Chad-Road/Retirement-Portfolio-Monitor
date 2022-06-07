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

if __name__ == "__main__":
    pass
