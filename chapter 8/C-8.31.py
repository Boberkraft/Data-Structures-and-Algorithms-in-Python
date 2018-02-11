"""
Define the internal path length, I(T), of a tree T to be the sum of the
depths of all the internal positions in T. Likewise, define the external path
length, E(T), of a tree T to be the sum of the depths of all the external
positions in T. Show that if T is a proper binary tree with n positions, then
E(T) = I(T) +n−1.

Ofcurse i can do this with EulerTour but im lazy!


So firstly lest calculate number of internel and external nodes
External = Internal + 1
ok easy, now what?


Because every internal is a child of external with depth + 1
then
E(T) = I(T) 

Mamy drzewo o wysokości h

n = i + e
n = i + i + 1
n = 2i + 1
(n - 1)/2 = i
E(T) = I(T) +n−1.
I(t) = E(t) - n + 1
Indukcja:
Założenia
n = 1:
E(t) = 0
I(t) = 0

Mamy sobie drzewo T0

Zakładamy, że T1 ma r wezłów wewnętrznych
To T2 ma n/2 - r - 3/2 węzłów wewnętrznych
Węzły w T1
n1 = 2r + 1
Węzły w T2
n2 = n-2r-2



E(T) = I(T) + n − 1
E(T1) = I(T1) + 2r
E(T2) = I(T2) + (n-2r - 2) - 1
E(T2) = I(T2) + n - 2r - 3

Przez to że usuneliśmy roota, to każdy węzeł z podrzew stracił 1 punkt.
Jak teraz dodamy tego rota, to powinno być gites.
łącznie całe drzewe straciło tyle punktów ile jest liści. 
                    
E(T) = I(T) + n − 1.
     
E(T) =            
    E(T1) + (r + 1) +  E(T2) + (n/2 - r - 1/2)
    E(T1) + r + 1 +  E(T2) + n/2 - r - 1/2
    E(T1) +  E(T2) + n/2 + 1/2
    I(T1) + 2r + I(T2) + n - 2r - 3 + n/2 + 1/2
    I(T1) + I(T2) - 5/2 + 3n/2

I(T) =
    I(T1) + r + I(T2) +  n/2 - r - 3/2
    I(T1) + I(T2) +  n/2 - 3/2

WIELKI FINAł
E(T) = I(T) + n − 1
I(T1) + I(T2) - 5/2 + 3n/2 = I(T1) + I(T2) +  n/2 - 3/2 + n − 1
- 5/2 + 3n/2 =  n/2 - 3/2 + 2n/2 − 1
- 5/2 + 3n/2 =  3n/2 - 3/2 − 2/2
- 5/2 + 3n/2 =  3n/2 - 5/2
0 = 0
HhahahaHAHAHAHAH
SGHERFSD
SDF

'
SDF
SDFS
DF
SDF

KURWA

CZEMU

"""


def I(T, position):
    # assume tree with 1 > nodes
    depth_descendants = 0
    if not T.is_leaf(position):
        for child in position:
            depth_descendants += I(T, child)
        return depth_descendants + T.depth(position)
    else:
        # its a leaf
        return 0


def E(T, position):
    # assume tree with 1 > nodes
    depth_descendants = 0
    if not T.is_leaf(position):
        for child in position:
            depth_descendants += I(T, child)
        return depth_descendants
    else:
        return depth_descendants + T.depth(position)
