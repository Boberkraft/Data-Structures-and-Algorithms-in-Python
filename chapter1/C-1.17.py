# Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
#   for val in data:
#       val *= factor
# Explain why or why not.

def scale(data, factor):
    for val in data:
        # it dont work because val is a new allias and its being broke with reasigment
        val *= factor

if __name__ == '__main__':
    data = [1,2,3,4]
    scale(data, 2)
    print(data)

