"""
https://math.stackexchange.com/questions/1196452/expected-value-of-the-number-of-flips-until-the-first-head?noredirect=1&lq=1

Let x be the expected number of flips. 
Then after the first flip half the time we stop and the other half the time we continue. 
That gives x=1+0.5(0)+0.5(x) and so x=2 or x is infinite. The latter is impossible (see note below) and hence x=2.

x = 1 + 0.5x
0.5x = 1
x = 2
"""
