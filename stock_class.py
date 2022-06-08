
class Stock:
    """
    
    """
    def __init__(self, symbol, name, shares):
        """
        Creates"""
        self.symbol = symbol
        self.name = name
        self.shares = shares
        self.DataList = []

    def add_data(self, stock_data):
        self.DataList.append(stock_data)

class DailyData:
    def __init__(self, date, close, volume):
        self.date = date
        self.close = close
        self.volume = volume


if __name__ == "__main__":
    pass