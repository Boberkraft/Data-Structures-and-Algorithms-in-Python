from creditcard import CreditCard


class PredatorCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    LIMIT_BEFORE_ADD = 10
    SURCHARGE = 5
    LATE_FEE = 0.02
    LATE_FEE_AMOUNT = 200

    def __init__(self, customer, bank, acnt, limit, apr):
        super(PredatorCreditCard, self).__init__(customer, bank. acnt, limit)
        self._apr = apr
        self._calls = 0
        self._last_balance = 0
        self._money_spend = 0

    def charge(self, price):
        self._calls += 1
        surcharge = 0
        if self._calls > PredatorCreditCard.LIMIT_BEFORE_ADD:
            surcharge = PredatorCreditCard.SURCHARGE
        success = super().charge(price + surcharge)
        if not success:
            self._balance += PredatorCreditCard.OVERLIMIT_FEE
        return success

    def make_payment(self, amount):
        super().make_payment(amount)
        self._money_spend += amount

    def process_month(self):

        late_fee = PredatorCreditCard.LATE_FEE_AMOUNT > self._money_spend
        if late_fee:
            amount = self.get_balance() * PredatorCreditCard.LATE_FEE
            super().charge(-amount)
        self._money_spend = 0
        self._calls = 0
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == '__main__':
    pass
