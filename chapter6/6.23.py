"""
Suppose you have three nonempty stacks R, S, and T. Describe a sequence
of operations that results in S storing all elements originally in T below all
of S’s original elements, with both sets of those elements in their original
order. The final configuration for R should be the same as its original
configuration. For example, if R = [1,2,3], S = [4,5], and T = [6,7,8,9],
the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5].

You can still use R as temporary storage, as long as you never
pop its original contents.

"""

r = [1, 2, 3]
s = [4, 5]
t = [6, 7, 8, 9]

# r <- s
# r <- t
# t <- r (not first 3)

to_pop = len(s) + len(t)
for _ in range(len(s)):
    r.append(s.pop())
for _ in range(len(t)):
    r.append(t.pop())

for _ in range(to_pop):
    s.append(r.pop())
print(r, s, t)
