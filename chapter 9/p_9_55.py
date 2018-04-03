"""
Write a program that can process a sequence of stock buy and sell orders
as described in Exercise C-9.50.

I SHOULD HAVE ADDED A METHOD TO UPDATE VALUE OF ROOT
"""

from AdaptableHeapPriorityQueue import AdaptableMaxHeapPriorityQueue
from AdaptableHeapPriorityQueue import AdaptableMinHeapPriorityQueue


# --------------------------------- just a trick
def update(self, new_key):
    if self.is_empty():
        raise Exception()

    self._data[0]._key = new_key
    self._buble(0)


AdaptableMinHeapPriorityQueue.update = update
AdaptableMaxHeapPriorityQueue.update = update


# ----------------------------------

class Stock:
    def __init__(self):
        self._buy_orders = AdaptableMaxHeapPriorityQueue()
        self._sell_orders = AdaptableMinHeapPriorityQueue()

    def add_sell_order(self, quantity, value):
        self._sell_orders.add(quantity, value)
        self._check()

    def add_buy_order(self, quantity, value):
        self._buy_orders.add(quantity, value)
        self._check()

    def _check(self):
        """Do the buying stuff"""
        if self._sell_orders.is_empty() or self._buy_orders.is_empty():
            return

        b_want, b_for_each = self._buy_orders.max()
        s_got, s_cost = self._sell_orders.min()
        how_many = 0
        if b_for_each >= s_cost:
            if b_want >= s_got:
                # remove a sale
                self._sell_orders.remove_min()
                how_many = s_got
            else:
                self._sell_orders.update(s_got - b_want)

            if s_got >= b_want:
                # remove offert
                self._buy_orders.remove_max()
                how_many = b_want
            else:
                self._buy_orders.update(b_want - s_got)

            print('Someone bought', how_many, 'sales for', b_for_each, '$ each')
            self._check()

    def print_buyers(self):
        print('Buyers:')
        for k, v in self._buy_orders:
            print('\tWant', -k, 'sales for', v, '$')

    def print_sellers(self):
        print('Sellers:')
        for k, v in self._sell_orders:
            print('\tSells', k, 'sales for', v, '$')


market = Stock()
market.add_sell_order(100, 20)
market.add_sell_order(50, 40)
market.add_sell_order(51, 20)
market.add_sell_order(61, 10)
market.print_sellers()
print()
# market.add_buy_order(50, 5)
market.add_buy_order(5, 40)
# market.add_buy_order(2, 7)
market.print_sellers()
market.print_buyers()
# market.add_buy_order(2, 4)