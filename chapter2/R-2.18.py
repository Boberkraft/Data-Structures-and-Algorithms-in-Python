from fibonacciprogression import FibonacciProgression

if __name__ == '__main__':
    for x, num in enumerate(FibonacciProgression(2, 2)):
        if x+1 >= 8:
            print(num)
            break

    for x, num in enumerate(FibonacciProgression(2, 2)):
        print("{} -> {}".format(x+1, num))
        if x >= 8:
            break