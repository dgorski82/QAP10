class Investment:
    def __init__(self, invest_time, invest_summa):
        self.invest_time = invest_time
        self.invest_summa = invest_summa


class Bank:

    def __init__(self, rate=0.1):
        self.rate = rate

    def deposit(self, summa, time):
        rate = self.rate
        month_rate = rate / 12
        for i in range(time):
            for y in range(12):
                summa = summa + (summa * month_rate)
                print(f"year - {i}, month - {y + 1}, month_sum - {summa * month_rate} summ - {summa}")


new_investment = Investment(2, 10)

bank = Bank()

summ = new_investment.invest_summa
tim = new_investment.invest_time

bank.deposit(summ, tim)
