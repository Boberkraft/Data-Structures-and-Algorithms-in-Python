"""
The quadratic probing strategy has a clustering problem related to the way
it looks for open slots. Namely, when a collision occurs at bucket h(k), it
checks buckets A[(h(k)+i^2) mod N], for i = 1,2,...,N - 1.


For part a, note that the symmetry will halve the range of possible
values. For part b, note that such automatic collisions will not occur

------------------------------------ a -------------------------------

a. Show that i^2 mod N will assume at most (N +1)/2 distinct values,
   for N prime, as i ranges from 1 to N - 1. As a part of this 
   justification, note that i^2 mod N = (N - i)^2 mod N for all i.
   

a prime 97

i = 4
i^2 = 16


16 mod 97 = 16

(97 - 4)^2 mod 97 = 16
(97 - 4)**2 % 97 = 16

     (N - i) ^ 2 mod N  = i^2 mod N
N^2 - 2*N*i + i^2 mod N = i^2 mod N
N(N - 2*i) + i^2  mod N = i^2 mod N
(because mod N strips N, we can remove it) 
              i^2 mod N = i^2 mod N

(so yea! it's True)

So you see... 
(-i)^2 = i^2 -> 2 dinstinct values give one output

SO

lets suppose your N is 10.

i
<--------
x x   x       x
1 2 3 4 5 6 7 8 9 10
            
          --------->
             10 - i
             
AT SOME POINT they are going to be the same values
So i will call it, that they can give you N/2 distinct values
and if N if odd (like prime) then it's (N+1)/2

Example - for mod 7. 

1^2 = 6^2 = 1. 
2^2 = 5^2 = 4. 
3^2 = 4^2 = 2. 

EXAMPLE
Lets supose your hashing functions is 
i^2 for i in {0,1,2,3,4,5,6}
0^2 = 0
1^2 = 1
2^2 = 4
3^2 = 2
4^2 = 2
5^2 = 4
6^2 = 1
And from our definition
we can represent all other values i >= N as (cN - i)^2 => 4N^2 - 4Ni + i^2 => i^2 
(c*N where c is a natural number, for this c = 2 )
7^2 = 0
8^2 = 1
9^2 = 4
...


i
<--------
x x x  x       
0 1 2 3 4 5 6 7
            
          --------->
             10 - i

https://stackoverflow.com/a/29057857/6244503
I have added myself the part for i > N

N^2 - 2*N*i + i^2 
N(N - 2*i) + i^2
N(N - 2*i) + i^2 
-N + i^2

You can also think  of (N - i) ^ 2 mod N  = i^2 mod N

as N being 0
and then f(N + x) -> F(x)
         f(N - x) -> F(x)
just like (-i)^2 = i^2 -> 2

------------------------------------ b -------------------------------
   
b. A better strategy is to choose a prime N such that N mod 4 = 3 and
   then to check the buckets A[(h(k) ± i^2) mod N] as i ranges from 
   1 to (N - 1)/2, alternating between plus and minus. Show that this
   alternate version is guaranteed to check every bucket in A.

i in {1,2,3,4,5}
0 1 2 3 4 5 6 7 8 9 10
====================== + i^2
  1   3 4 5       9
  
====================== - i^2
    2        6 7 8  10


it havent checked 0 but i will ignore it for now 


So we know that + i^2 can generate N/2 distinct values.
We can't generate more, because then function i^2 works like this one -> (N-i)^2

If N = 9
its like
        i = 0 1 2 3 4 5 6 
i^2 mod 9 = 0 1 4 2 2 4 1

As we can see, the second half is just a copy: let's do something with it!
As you can see, it work's form the 'end'.

         i = 0 1 2 3 4 5 6 
-i^2 mod 9 = 0 6 3 5 5 3 6




































"""