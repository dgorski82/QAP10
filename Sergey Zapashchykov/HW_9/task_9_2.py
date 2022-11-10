class Investment:

    PERCENT = 0.1

    def __init__(self, quantity: int, term: int):
        self.quantity = quantity
        self.term = term


class Bank:

    @classmethod
    def deposit(cls, contribution):
        for _ in range(contribution.term * 12):
            contribution.quantity = contribution.quantity + (contribution.quantity * (Investment.PERCENT / 12))
        return round(contribution.quantity, 2)


investment1 = Investment(100, 3)
calculate = Bank.deposit(investment1)
print(calculate)
