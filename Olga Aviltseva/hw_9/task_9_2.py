class Investment:

    def __init__(self, sum_inv, period, percent):
        self.sum_inv = sum_inv
        self.period = period
        self.percent = percent


class Bank:

    @classmethod
    def deposit(cls, investment: Investment):
        for month in range(investment.period * 12):
            investment.sum_inv += investment.sum_inv * investment.percent / 1200
        return investment.sum_inv


print(f'Total money: {Bank.deposit(Investment(1000, 5, 10))}')
