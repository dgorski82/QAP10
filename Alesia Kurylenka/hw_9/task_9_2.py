class Investment:

    def __init__(self, investment_amount, investment_term):
        self.investment_amount = investment_amount
        self.investment_term = investment_term


class Bank:

    @classmethod
    def deposit(cls, n, r):
        m = r * 12
        percent = 10
        calculated_summa = n * (1 + percent / (12 * 100)) ** m
        print(f"Rounded result of your investment calculation:: {round(calculated_summa)}")
        return calculated_summa


my_investment = Investment(30000, 10)
calculation = Bank.deposit(my_investment.investment_amount, my_investment.investment_term)
