class Investment:

    INVESTMENT_PERCENT = .1

    def __init__(self, summa: float, period: int):
        self.summa = summa
        self.period = period


class Bank:

    @classmethod
    def deposit_info(cls, n, r):
        invest.summa = n
        for i in range(1, r * 12 + 1):
            n = n + (n * Investment.INVESTMENT_PERCENT / 12)
        return n - invest.summa


invest = Investment(10000, 1)
print(f'Total profit: {Bank.deposit_info(invest.summa, invest.period)}')
