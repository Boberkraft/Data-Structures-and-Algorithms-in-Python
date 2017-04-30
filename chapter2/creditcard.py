
class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def _set_balance(self, b):
        self._balance = b

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError('Amount cannot be negative')

        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings',
                             '9653 2234 1223 2121', 2500))
    wallet.append(CreditCard('John Bowman', 'California Savings',
                             '9123 24234 1233 2121', 350))
    wallet.append(CreditCard('John Bowman', 'California Savings',
                             '3122 2234 1233 2421', 5000))

    for val in range(1, 20):
        for x, wall in enumerate(wallet):
            if not wall.charge(val * (x + 1)):
                print(wall.get_account(), 'limit')

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()

