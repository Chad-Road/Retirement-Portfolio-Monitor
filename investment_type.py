from stock_class import Stock

class Investment:
    """ General class of investments excluding maturation based investments (e.g. stock, funds, etc.)"""

    def __init__(self, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, other_fees):
        self.initial_value = initial_value 
        self.mean_return = mean_return
        self.return_risk = return_risk
        self.expected_tax = expected_tax
        self.liquidity_penalty = liquidity_penalty
        self.other_fees = other_fees

    def add_inv(self):
        pass


class MaturationBased(Investment):
    """ Sub-class of maturation based investments including bonds, IRAs, and 401ks"""

    def __init__(self, initial_value, mean_return, return_risk, expected_tax, liquidity_penalty, maturation_time, early_penalty):
        super().__init__(initial_value, mean_return, return_risk, expected_tax, liquidity_penalty)
        self.maturation_time = maturation_time
        self.early_penalty = early_penalty

    def add_ma_inv(self):
        pass


if __name__ == "__main__":
    pass
