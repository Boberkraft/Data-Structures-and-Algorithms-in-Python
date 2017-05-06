
def power(x, n):
    if n == 0:
        return 1
    else:
        parial = power(x, n//2)
        result = parial * parial
        if n % 2 == 1:
            result *= x
        return result

if __name__ == '__main__':
    print(power(2,5))