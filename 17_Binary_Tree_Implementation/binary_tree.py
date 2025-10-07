# Binary Tree Implementation in Python

# Importing LinkedListQueue for level-order insertion
from linked_list_based_queue import LinkedListQueue

# Creating a TreeNode class to represent each node in the binary tree containing data, left child, and right child
# And Can add Parent pointer if needed


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        # self.parent = None  # Optional parent pointer

# Creating a BinaryTree class to manage the binary tree operations


class BinaryTree:
    # Constructor to initialize the binary tree with a root node
    def __init__(self):
        self.root = None

    # 1- Insertion (Level-order)
    # Insert a new node in level-order to keep the tree complete
    def insert(self, data):
        # Create a new node from data
        new_node = TreeNode(data)
        # If tree is empty, set new node as root
        if self.root is None:
            self.root = new_node
            return
        # Else
        # Create a queue for level-order traversal
        queue = LinkedListQueue()
        # Start with the root node
        queue.en_queue(self.root)
        # Loop until we find an empty spot
        while not queue.is_empty():
            # Dequeue the front node [dequeue means remove and return the front node]
            current_node = queue.de_queue()
            # Check if left child is None, if so, insert the new node here
            if current_node.left_child is None:
                current_node.left_child = new_node
                break
            else:
                # Else enqueue the left child for further exploration [enqueue means add to the back of the queue]
                queue.en_queue(current_node.left_child)

            # Check if right child is None, if so, insert the new node here
            if current_node.right_child is None:
                current_node.right_child = new_node
                break
            else:
                # Else enqueue the right child for further exploration
                queue.en_queue(current_node.right_child)

    # 2- Height Calculation
    # Calculate the height of the tree (number of edges in longest path from root to leaf)
    # [Height mean number of levels in the tree]
    def height(self, node=None):
        return self.internal_height(self.root)

    # Helper function to calculate height recursively
    def internal_height(self, node):
        # Base case: if node is None, height is 0
        if node is None:
            return 0
        # Else return 1 + max height of left and right subtrees
        # This makes recursion and recall the function for left until reach the base case
        # And after that recall the function for right until reach the base case
        # After that it will return the max height between left and right subtree + 1 for the current node
        return 1 + max(self.internal_height(node.left_child), self.internal_height(node.right_child))

    # 3- Tree Traversals
    # Pre-order Traversal (Root, Left, Right)
    def pre_order_traversal(self, node):
        self.internal_pre_order_traversal(node)
        print()

    def internal_pre_order_traversal(self, node):
        if node is None:
            return
        # Recursively traverse the tree in pre-order manner (root, left, right)
        print(node.data, "-->", end=" ") # Visit the root
        self.internal_pre_order_traversal(node.left_child) # Traverse left
        self.internal_pre_order_traversal(node.right_child) # Traverse right

    # In-order Traversal (Left, Root, Right)
    def in_order_traversal(self, node):
        self.internal_in_order_traversal(node)
        print()

    def internal_in_order_traversal(self, node):
        if node is None:
            return
        # Recursively traverse the tree in in-order manner (left, root, right)
        self.internal_in_order_traversal(node.left_child) # Traverse left  
        print(node.data, "-->", end=" ") # Visit the root
        self.internal_in_order_traversal(node.right_child) # Traverse right

    # Post-order Traversal (Left, Right, Root)
    def post_order_traversal(self, node):
        self.internal_post_order_traversal(node)
        print()

    def internal_post_order_traversal(self, node):
        if node is None:
            return
        self.internal_post_order_traversal(node.left_child) # Traverse left
        self.internal_post_order_traversal(node.right_child) # Traverse right
        print(node.data, "-->", end=" ") # Visit the root

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node.right_child:
            self.print_tree(node.right_child, prefix +
                            ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
        if node.left_child:
            self.print_tree(node.left_child, prefix +
                            ("    " if is_left else "│   "), True)


if __name__ == "__main__":

    binary_tree = BinaryTree()
    # binary_tree.insert(1)
    # binary_tree.insert(2)
    # binary_tree.insert(3)
    # binary_tree.insert(4)
    # binary_tree.insert(5)
    # binary_tree.insert(6)
    # binary_tree.insert(7)

    binary_tree.insert("A")
    binary_tree.insert("B")
    binary_tree.insert("C")
    binary_tree.insert("D")
    binary_tree.insert("E")
    binary_tree.insert("F")
    binary_tree.insert("G")
    binary_tree.insert("H")
    binary_tree.insert("I")

    print("Height of tree:", binary_tree.height())

    print("Pre-order Traversal:")
    binary_tree.pre_order_traversal(binary_tree.root)

    print("In-order Traversal:")
    binary_tree.in_order_traversal(binary_tree.root)

    print("Post-order Traversal:")
    binary_tree.post_order_traversal(binary_tree.root)

    binary_tree.print_tree()
