from random import randint
while True:
    x = randint(5,9)
    y = randint(5,9)
    print('{} * {} = '.format(x,y),end='')
    if int(input()) != x*y:
        print('źle ', x*y)