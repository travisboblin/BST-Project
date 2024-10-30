from bstnode import BSTNode

"""
The code to implement a binary search tree. You must fill in all of the methods
below (and remove the `pass`) as explained in the comments and by the usage in
main.py.

Feel free to add any additional helper functions, but DO NOT modify the names or
required inputs of the functions as indicated. Adding optional inputs is fine, however.

NOTE: The tree, upon creation, has no nodes; the root is empty. Do not forget to update
self.root when the root changes (e.g. inserting the first node into an empty tree or
removing the last node).

"""

class BST:
    def __init__(self):
        self.root = None

    # Return the root of the BST
    def get_root(self) -> BSTNode:
        return self.root

    """
    Recursively search for the key in `key` using the binary search tree property.
    Recall that this property says, for any specific node, all of its left children's keys
    are smaller, and all of its right children's keys are larger.
    
    Args:
        key: integer key that you are searching for
        node: the node we are currently checking
        
    Return:
        Returns the BSTNode with key equal to `key` if found, or None otherwise
    """

    def search(self, key: int, node: BSTNode) -> BSTNode|None:
        pass

    """
    Insert the given node at the correct position in the binary search
    tree using the BST property (defined in search() above). If the next
    node you would visit doing this search is None, that's where the node
    should be inserted. If the node already exists, do nothing.
    
    You will be inserting into the tree a new instance of BSTNode(key).
    
    If your tree is empty, don't forget to update the root!

    Args:
        key: integer key that you are adding to the tree

    Return:
        None
    """

    def insert(self, key: int) -> None:
        pass

    """
    Delete a node with given `key` from the tree.

    Deletion is the most complex task in a binary search tree. First, you must search for
    the node you wish to delete. If it doesn't exist, we're done - nothing to delete.
    
    If it does, and it is the only node (it is the root AND has no children), update self.root to None.
    
    Otherwise, there are three situations to consider:
        1) The node has no children (is a leaf node). Update its parent (if it exists) to no
        longer point to it and it is now removed from the tree.
        2) The node has one child. Copy that child's key to the current node and "remove" that child by
        setting its left/right child property to None.
        3) (BONUS MARKS) The node has two children. Find this node's successor. That means find the minimum
        of node.right_child. Replace this node's key with that one. Now look down node.right_child to delete
        the key you just found (it should always be a leaf node so you can perform those steps above).
    
    After deleting, don't forget to update self.root if it has changed!
    
    Args:
        key: integer key that you are deleting from the tree

    Returns:
        The key that was asked to be deleted, and if it is not in the tree, return None
    """

    # Helper function to find the smallest key starting at node
    def minimum(self, node: BSTNode) -> BSTNode:
        pass

    def delete(self, key: int) -> int|None:
        pass

    """
    Recursively perform the given traversal of the tree.
    
    Preorder: Visit node, left child, right child in that order
    Inorder: Visit left child, node, right child in that order
    Postorder: Visit left child, right child, node in that order
    
    Args:
        node: node we're looking to traverse from.
        
    Returns:
        A list of the keys of the nodes visited.
    """

    def preorder(self, node: BSTNode) -> list[int]:
        pass

    def inorder(self, node: BSTNode) -> list[int]:
        pass

    def postorder(self, node: BSTNode) -> list[int]:
        pass
