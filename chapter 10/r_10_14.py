"""
 Show the result of rehashing the hash table shown in Figure 10.6 into a
table of size 19 using the new hash function h(k) = 3k mod 17.
"""

from time import sleep

table = [[] for _ in range(13)]

for x in [54, 28, 41, 18, 10, 36, 25, 38, 12, 90]:
    hh = (3 * x) % 13
    table[hh].append(x)

    print(table)
print()
for x in table:
    print(x)