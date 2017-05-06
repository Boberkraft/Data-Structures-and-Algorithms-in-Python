
def convert_to_base(number, base):
    if number == 0:
        return [0]

    digits = []
    while number:
        digits.append(number % base)
        number = number//base
    answer = reversed(digits)
    return list(answer)

if __name__ == '__main__':
    # f = 15
    num = 2**64-1
    print(convert_to_base(num, 16))
    print(hex(num))