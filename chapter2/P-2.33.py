# Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the first derivative of that polynomial.

class Polynomial:
    spacing = {' ', '+', '-'}
    def __init__(self, formula):
        self.formula = '{} '.format(formula)
        self._stack = []
        self._parsed = []
        self._open_b = []
        self._close_b = []
        self._last = 0
        self.parse()

    def parse(self):
        for index, letter in enumerate(self.formula):
            if letter == '(':
                self._open_b.append(index)
            elif letter == ')':
                self._close_b.append(index)

            elif letter in Polynomial.spacing:
                if len(self._open_b) == len(self._close_b):
                    new = self.formula[self._last: index].strip()
                    if new != '':
                        self._stack.append(new)

                        self._last = index
        # print(self._stack)

    def get_pow(self, term):
        open_b = []
        close_b = []
        start = 0
        end = 0
        for index, letter in enumerate(term):
            if letter == '(':
                open_b.append(index)
            if letter == ')':
                if start != 0:
                    end = index
                close_b.append(index)
            if len(open_b) == len(close_b):
                if letter == '^':
                    start = index
        if start == end:
            return 0, 0
        return start+2, end
    def __str__(self):
        return self.formula

    def derivative(self):
        end_stack = []
        for intex, term in enumerate(self._stack):
            if term not in Polynomial.spacing:
                start, end = self.get_pow(term)
                try:
                    pow = int(term[start:end])
                except ValueError:
                    pow = -1
                if pow - 1 < 0:
                    try:
                        del end_stack[-1]
                    except KeyError:
                        pass
                    continue
                new = list(term)
                new[start:end] = [pow - 1]
                end = str(pow)
                for x in new:
                    end += str(x)
                new = end
                term = new
            end_stack.append(term)
        return ' '.join(end_stack)

if __name__ == '__main__':
    # ohh sheet my internet dont work so i cant check for better solution :/

    x = Polynomial('xa^(4) - (y + 2)b^(3) + zc^(2) + yd')
    print(x)
    print(x.derivative())




