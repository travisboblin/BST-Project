from typing import Optional

"""
Binary search tree node object. On creation, pass the key.

left_child and right_child are assumed to be either None or another
valid BSTNode.

The parent is similarly either None or another valid BSTNode. You may
or may not need to use this property depending on your implementation.
If you don't use it, you can leave it as None on all nodes, I will not
be explicitly checking for it.

Usage: node = BSTNode(5)
"""

class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left_child: Optional[BSTNode] = None
        self.right_child: Optional[BSTNode] = None
        self.parent: Optional[BSTNode] = None
