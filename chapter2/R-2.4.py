
class Flower:

    def __init__(self, name, petels, price):
        self._name = name
        self._petels = petels
        self._price = price


    @property
    def price(self):
        print('returni name')
        return self._price

    @price.setter
    def price(self, price):
        print('setting mgae')
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def petels(self):
        return self._petels

    @petels.setter
    def petels(self, num):
        self._petels = num


if __name__ == '__main__':
    x = Flower('Toy', 2, 32)
    print(x.price)
    print(x.petels)
    print(x.name)
