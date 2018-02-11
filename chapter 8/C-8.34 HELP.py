"""
For a tree T, let nI denote the number of its internal nodes, and let nE
denote the number of its external nodes. Show that if every internal node
in T has exactly 3 children, then nE = 2nI +1.

So:
1
3
9
NO PROBLEMOOOOOOOOO
INDUCTION IS FOR LESZCZE
is there algebraic solution?

Internal nodes are just geometric series and then bum:
internal nodes = sum 3^a for a=0..x
external nodes = 3^x
Lets plug it in 2nT + 1 = nE
Lets plug it in 2nI + 1 - nE = 0
and im lazy. Do it yourself!
http://www.wolframalpha.com/input/?i=2(sum+3%5Ea+for+a%3D0..(x-1))+%2B+1+-+3%5Ex
"""
