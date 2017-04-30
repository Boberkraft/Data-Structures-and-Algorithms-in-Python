# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible

from decimal import Decimal

def change(charged, returned, monetary=
[200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]):
    def deepest(num):
        for monet in monetary:
            if num - Decimal(str(monet)) >= 0:
                return monet
    rest_bills = []
    rest = Decimal(str(charged)) - Decimal(str(returned))
    while rest > 0:
        new_bill = deepest(rest)
        rest_bills.append(new_bill)
        rest -= Decimal(str(new_bill))
    return rest_bills

if __name__ == '__main__':
    print(change(100, 99.56))
