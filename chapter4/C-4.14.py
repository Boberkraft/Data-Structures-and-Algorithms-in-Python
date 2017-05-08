"""
In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
the next, so that the smallest is on the top and the largest is on the bottom.
The puzzle is to move all the disks from peg a to peg c, moving one disk
at a time, so that we never place a larger disk on top of a smaller one.
See Figure 4.15 for an example of the case n = 4. Describe a recursive
algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
Consider first the subproblem of moving all but the nth disk from peg a to
another peg using the third as “temporary storage.”)

Ok so this are my rules:
Move largest disk on larger disk. If cant, move to free space.
Disks cant go back.

but i dont feel its really recursive so i watched a video on youtube
https://www.youtube.com/watch?v=q6RicK1FCUs

"""

class Tower:
    def __init__(self, disks):
        self.disks = disks
        self.pegs = [[disks for disks in range(disks, 0, -1)], [], []]

    def move(self, source, dest):
        pegs = self.pegs

        if len(pegs[source]) > 0:
            de = pegs[dest]
            if len(de) == 0:
                de = self.disks + 1
            else:
                de = de[-1]
            if pegs[source][-1] < de:
                pegs[dest].append(pegs[source].pop())
            else:
                print('Error. Cont move {} to {}'.format(source, dest))
                quit()
        else:
            print('What have you done? Cant move empty')
            quit()


# def solve1(tower, values, last):
#     """Move large disk on larger disk. If cant, move to free space.
# Disks cant go back."""
#
#     # DONT WORKS
#     s = sorted(values, key=lambda x:x[1])[::-1]
#
#     largest = s[0]
#     large = s[1]
#
#     if large[0] == last:
#         # if selected the same disk
#         large = s[2]
#     if large[1] == 0:
#         # if selected disk is /none/
#         large, largest = largest, large
#     print('dont move to', last)
#     print('moving from',large[0], 'to', largest[0])
#
#     exposed = tower.move(large[0], largest[0])
#     print('Tower', tower.pegs)
#     values[large[0]][1], values[largest[0]][1] = exposed, large[1]
#     print('*'*10)
#     solve(tower, values, largest[0])


def solve(disk, source, temp, dest):
    global tower

    if disk > 0:
        solve(disk-1, source, dest, temp)  # move n-1 disks to temp
        tower.move(source, dest)  # move biggest to dest
        solve(disk-1, temp, source, dest)  # move middle to dest



if __name__ == '__main__':

    tower = Tower(3)
    solve(3, 0, 2, 1)

