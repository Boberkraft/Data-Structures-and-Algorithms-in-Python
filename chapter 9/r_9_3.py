"""
What does each remove min call return within the following sequence of
priority queue ADT methods: add(5,A), add(4,B), add(7,F), add(1,D),
remove min( ), add(3,J), add(6,L), remove min(), remove min(),
add(8,G), remove min(), add(2,H), remove min(), remove min()?


add(5,A), (5) -> 5
add(4,B), (4, 5) -> 4
add(7,F), (4, 5, 7) -> 7
add(1,D), (1, 4, 5, 7) -> 1
remove min( ), (4, 5, 7) -> 1
add(3,J), (3, 4, 5, 7) -> 3
add(6,L), (3, 4, 5, 6, 7) -> 6
remove min(), (4, 5, 6, 7) -> 3
remove min(), (5, 6, 7) -> 4
add(8,G), (5, 6, 7, 8) -> 8
remove min(), (6, 7, 8) -> 5
add(2,H), (2, 6, 7, 8) -> 2
remove min(), (6, 7, 8) -> 2
remove min() (7, 8) -> 6

"""