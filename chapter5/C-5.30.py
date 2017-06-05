"""
When Bob wants to send Alice a message M on the Internet, he breaks M
into n data packets, numbers the packets consecutively, and injects them
into the network. When the packets arrive at Alice’s computer, they may
be out of order, so Alice must assemble the sequence of n packets in order
before she can be sure she has the entire message. Describe an efficient
scheme for Alice to do this, assuming that she knows the value of n. What
is the running time of this algorithm?

Its O(n) without even creatinh hash table
"""

from io import StringIO

init = """\
3\tcute 
0\tthe 
4\t!
2\tis 
1\tword 
"""

network = StringIO(init)

def get_message(n, f):
    # n = number of segments
    got = 0
    data = [None] * n
    while got < n :
        curent = f.readline().rstrip('\n').split('\t')
        data[int(curent[0])] = curent[1]
        got += 1
    return ''.join(data)


if __name__ == '__main__':

    print(get_message(5, network))
