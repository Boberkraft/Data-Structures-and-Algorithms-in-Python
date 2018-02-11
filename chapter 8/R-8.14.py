"""
Justify Table 8.2, summarizing the running time of the methods of a tree
represented with a linked structure, by providing, for each method, a description
of its implementation, and an analysis of its running time.

Operation Running Time
len, is empty                   O(1)
root, parent, is root, is leaf  O(1)
children(p)                     O(cp +1)
depth(p)                        O(dp +1)
height                          O(n)
We let cp denote the number of children of a
position p. The space usage is O(n).

len. Fancy is_empty
There is special variable just for size.
Checking value of variable have constant time.

root, parent, is root, is leaf.
Each node is have variable for its parent and its children.
In each tree there is a variable for storing root node.
Is leaf checks if node have at least one children.
Parent just check variable associated with parent.

children
Why its O(cp + 1)? I dont know from where that one comes from.
Because it firsly needs to check if there len(children) > 0?
or because if it dont have children then saying that
something is O(0) is stupid thus + 1, because a node can have
0 children?
its O(cp) because it iterates over all children od p (cp).

depth(p)
because algorithm calls itself on every ancestor of p (depth) and
at itself (+ 1)

height
Its called at descendants of root, and then at descendants of descendants.
Because every node (excluding root) is a child of other node it is called
on every node (including root, because we started from it)

algorithm spends O(cp) time (depending on number of node children)
at each position.
We know that every node (excluding root) have a parent, so
sum(childrens) is n.

"""