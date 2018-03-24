"""
Show that the sum:

sum log i for i=0...n
 
which appears in the analysis of heap-sort, is Ω(n log n).

Because of:

log a*c = log a + log c

we can do log (mul i *  for i=0 ... n)
and its log (n!)

but uh... where i can go with it?

sum log i for i=0...n > log(n/2) + log(n/2 + 1) + log(n/2 + 2) + ... + log(n)
                      > log(n/2) + log(n/2) + log(n/2) + ... + log(n/2)
                      = n/2 * log(n/2)
                       
log (n!) < log ( n ^ n)
         = n log n

log (n!) > log ( n/2 ^ n/2)
         = n/2 log n/2
         = 1/2 * n log( 1/2 * n)
         = 1/2 * n log(1/2) * log(n)
         = 1/2 log(1/2) * n * log(n)
         c = 1/2 log(1/2) 
         = c * n * log(n)
         and it is Ω(n log n)  

"""
