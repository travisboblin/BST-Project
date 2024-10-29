from bst import BST
from bstnode import BSTNode

"""
Sample code showing off how each method is expected to be used.
These both explain the expectations while also acting partially
as unit tests for your code.

NOTE: These are not NECESSARILY enough to test your code fully!
These are just me showing you how the code would be used.
Make sure to test lots of cases!
"""

# Explaining how the BSTNode object is used
sample = BSTNode(5)
sample.left_child = BSTNode(3)
sample.right_child = BSTNode(8)
left_child = sample.left_child
right_child = sample.right_child
left_child.parent = sample
right_child.parent = sample

# The left and right children MUST be instances of BSTNode, not a value
# You will fail most tests if it's not!
print(f"Value: {sample.key}")
print(f"Left child (is an object): {left_child}, left child key: {left_child.key}")
print(f"Right child (is an object): {right_child}, left child key: {right_child.key}")

# In order to use a tree, you must first initialize it
# NOTE: You should only need to create BSTNode instances in your BST implementation
tree = BST()

# Add some nodes
tree.insert(15)
tree.insert(10)
tree.insert(12)
tree.insert(20)
tree.insert(23)

# Grab our root node
root = tree.get_root()

# Search for a node
assert tree.search(20).key == 20 # Exists
assert not tree.search(30) # Doesn't exist, returns None

# Find the minimum in the tree
assert tree.minimum(root) == 10

# Find the minimum from a specific node
assert tree.minimum(root.right_child) == 20

# Delete these nodes
assert tree.delete(12) == 12 # Exists so should return 12
assert not tree.delete(30) # Does not exist so returns None

# Perform the traversals
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
