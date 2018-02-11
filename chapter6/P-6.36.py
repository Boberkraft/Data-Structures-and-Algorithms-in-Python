"""
When a share of common stock of some company is sold, the capital
gain (or, sometimes, loss) is the difference between the share’s selling
price and the price originally paid to buy it. This rule is easy to understand
for a single share, but if we sell multiple shares of stock bought
over a long period of time, then we must identify the shares actually being
sold. A standard accounting principle for identifying which shares of
a stock were sold in such a case is to use a FIFO protocol—the shares
sold are the ones that have been held the longest (indeed, this is the default
method built into several personal finance software packages). For
example, suppose we buy 100 shares at $20 each on day 1, 20 shares at
$24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day
4 at $30 each. Then applying the FIFO protocol means that of the 150
shares sold, 100 were bought on day 1, 20 were bought on day 2, and 30
were bought on day 3. The capital gain in this case would therefore be
100 · 10+20 · 6+30 ·(−6), or $940. Write a program that takes as input
a sequence of transactions of the form “buy x share(s) at y each”
or “sell x share(s) at y each,” assuming that the transactions occur
on consecutive days and the values x and y are integers. Given this
input sequence, the output should be the total capital gain (or loss) for the
entire sequence, using the FIFO protocol to identify shares.



100 * (30 -20) + 20 * (30 - 24) + 30 * (30 - 36) = 940
"""

from ArrayQueue import ArrayQueue


class Sale:
    def __init__(self, quantity, price):
        self.qua = quantity
        self.price = price

    def __repr__(self):
        return "({} actions for {}$)".format(self.qua, self.price)


class Company:
    def __init__(self):
        self._actions = ArrayQueue()

    def buy(self, quantity, price):
        self._actions.enqueue(Sale(quantity, price))

    def sell(self, quantity, price):
        gain = 0
        while quantity > 0:
            latest = self._actions.first()
            if latest.qua <= quantity:
                gain += latest.qua * (price - latest.price)
                quantity -= latest.qua
                self._actions.dequeue()
            else:
                gain += quantity * (price - latest.price)
                latest.qua -= quantity
                quantity = 0
        return gain

    def __str__(self):
        return str(self._actions._data)


# 100     x $20   day 1
# 20      x $24   day 2
# 200     x $36   day 3
# -150     x $30   day 4
comp = Company()
comp.buy(100, 20)
comp.buy(20, 24)
comp.buy(200, 36)
print(comp.sell(150, 30))
# print(comp)
