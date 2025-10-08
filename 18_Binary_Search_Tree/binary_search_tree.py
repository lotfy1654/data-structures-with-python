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


class NodeAndParent:
    def __init__(self, node=None, parent=None, is_Left_Child=None):
        self.node = node
        self.parent = parent
        self.is_Left_Child = is_Left_Child


# Creating a BinaryTree class to manage the binary tree operations
class BinaryTree:
    # Constructor to initialize the binary tree with a root node
    def __init__(self):
        self.root = None

    # -----------------  Insertion (Level-order) -----------------

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

    # -----------------  Binary Search Tree Insertion -----------------

    # Insert a new node in the correct position to maintain BST properties
    def bst_insert(self, data):
        # Create a new node from data
        new_node = TreeNode(data)
        # If tree is empty, set new node as root
        if self.root is None:
            self.root = new_node
            return
        # Else, find the correct position to insert the new node
        current_node = self.root
        # Loop until we find the correct position
        while current_node is not None:
            # If data is less than current node's data, go left
            if data < current_node.data:
                # If left child is None, insert the new node here
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    break
                # Else, go left
                else:
                    current_node = current_node.left_child
            # If data is greater than or equal to current node's data, go right
            else:
                # If right child is None, insert the new node here
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    break
                # Else, go right
                else:
                    current_node = current_node.right_child

    # -----------------  Binary Search Tree Find -----------------

    def bst_find(self, data):
        current_node = self.root
        while current_node is not None:
            if data == current_node.data:
                return current_node
            # If data is less than current node's data, go left
            elif data < current_node.data:
                current_node = current_node.left_child
            # If data is greater than current node's data, go right
            else:
                current_node = current_node.right_child
        return None  # Not found

    # Return True if found, else False
    def find_or_none(self, data):
        return self.bst_find(data) is not None

    def find_with_parent(self, data):
        current_node = self.root
        parent_node = None
        is_Left_Child = None
        while current_node is not None:
            if data == current_node.data:
                return NodeAndParent(current_node, parent_node, is_Left_Child)
            elif data < current_node.data:
                parent_node = current_node
                is_Left_Child = True
                current_node = current_node.left_child
            else:
                parent_node = current_node
                is_Left_Child = False
                current_node = current_node.right_child
        return NodeAndParent(None, None, None)  # Not found

    # ----------------- Deletion -----------------

    # Main delete function
    def bst_delete(self, data):
        node_and_parent = self.find_with_parent(data)
        if node_and_parent.node is None:
            return False  # Node to delete not found

        # Case 1: Node is a leaf (no children)
        if node_and_parent.node.left_child is None and node_and_parent.node.right_child is None:
            self.del_is_leaf(node_and_parent)

        # Case 2: Node has one child [^ is XOR operator]
        elif (node_and_parent.node.left_child is not None) ^ (node_and_parent.node.right_child is not None):
            self.del_has_one_child(node_and_parent)

        # Case 3: Node has two children
        else:
            self.del_has_two_children(node_and_parent)

    # Case 1: Node is a leaf (no children)
    def del_is_leaf(self, node_and_parent):
        parent_node_to_del = node_and_parent.parent
        # Knowing if the node to delete is a left or right child of its parent
        if node_and_parent.is_Left_Child:
            # If the node to delete is a left child detach it from its parent
            parent_node_to_del.left_child = None
        else:
            # If the node to delete is a right child detach it from its parent
            parent_node_to_del.right_child = None

    # Case 2: Node has one child
    def del_has_one_child(self, node_and_parent):
        node_to_del = node_and_parent.node
        node_to_replace = None
        # Find the child of the node to delete
        if node_and_parent.node.left_child is not None:
            # If the left child is not None, it means the node to delete has a left child
            node_to_replace = node_and_parent.node.left_child
        else:
            # Else the node to delete has a right child
            node_to_replace = node_and_parent.node.right_child

        # Replace the node to delete with its child
        node_to_del.data = node_to_replace.data
        node_to_del.left_child = node_to_replace.left_child
        node_to_del.right_child = node_to_replace.right_child

        # Clear the reference to help with garbage collection
        node_to_replace = None

    # Case 3: Node has two children
    def del_has_two_children(self, node_and_parent):
        # Find the smallest node in the right subtree
        current_node = node_and_parent.node.right_child
        # Keep track of the node to delete
        node_to_del = node_and_parent.node
        # Keep track of the parent of the smallest node
        parent_smallest = None
        # Traverse to the leftmost node
        while current_node.left_child is not None:
            parent_smallest = current_node
            current_node = current_node.left_child

        # If the parent of the smallest node is not None, it means the smallest node is not the direct right child of the node to delete
        if parent_smallest is not None:
            parent_smallest.left_child = current_node.right_child
        else:
            # If the parent of the smallest node is None, it means the smallest node is the direct right child of the node to delete
            node_to_del.right_child = current_node.right_child
            node_to_del.data = current_node.data

    # ----------------- Balance Tree -----------------

    # Balance the tree to make it height-balanced
    def balance(self):
        nodes = []
        self.inorder_to_array(self.root, nodes)
        self.root = self.recursive_balance(0, len(nodes) - 1, nodes)

    # Helper function to perform in-order traversal and store nodes in an array
    def inorder_to_array(self, node, nodes):
        if node is None:
            return
        self.inorder_to_array(node.left_child, nodes)
        nodes.append(node.data)
        self.inorder_to_array(node.right_child, nodes)

    # Helper function to recursively build a balanced tree from the sorted array
    def recursive_balance(self, start, end, nodes):
        if start > end:
            return None
        mid = (start + end) // 2
        new_node = TreeNode(nodes[mid])
        new_node.left_child = self.recursive_balance(start, mid - 1, nodes)
        new_node.right_child = self.recursive_balance(mid + 1, end, nodes)
        return new_node

    # -----------------  Height Calculation -----------------

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

    # ----------------- Tree Traversals -----------------

    # Pre-order Traversal (Root, Left, Right)
    def pre_order_traversal(self, node):
        self.internal_pre_order_traversal(node)
        print()

    def internal_pre_order_traversal(self, node):
        if node is None:
            return
        # Recursively traverse the tree in pre-order manner (root, left, right)
        print(node.data, "-->", end=" ")  # Visit the root
        self.internal_pre_order_traversal(node.left_child)  # Traverse left
        self.internal_pre_order_traversal(node.right_child)  # Traverse right

    # In-order Traversal (Left, Root, Right)
    def in_order_traversal(self, node):
        self.internal_in_order_traversal(node)
        print()

    def internal_in_order_traversal(self, node):
        if node is None:
            return
        # Recursively traverse the tree in in-order manner (left, root, right)
        self.internal_in_order_traversal(node.left_child)  # Traverse left
        print(node.data, "-->", end=" ")  # Visit the root
        self.internal_in_order_traversal(node.right_child)  # Traverse right

    # Post-order Traversal (Left, Right, Root)
    def post_order_traversal(self, node):
        self.internal_post_order_traversal(node)
        print()

    def internal_post_order_traversal(self, node):
        if node is None:
            return
        self.internal_post_order_traversal(node.left_child)  # Traverse left
        self.internal_post_order_traversal(node.right_child)  # Traverse right
        print(node.data, "-->", end=" ")  # Visit the root

    # ----------------- Print Tree -----------------

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

    # binary_tree.insert("A")
    # binary_tree.insert("B")
    # binary_tree.insert("C")
    # binary_tree.insert("D")
    # binary_tree.insert("E")
    # binary_tree.insert("F")
    # binary_tree.insert("G")
    # binary_tree.insert("H")
    # binary_tree.insert("I")

    # Simple Binary Search Tree
    # binary_tree.bst_insert(1)
    # binary_tree.bst_insert(2)
    # binary_tree.bst_insert(3)
    # binary_tree.bst_insert(4)
    # binary_tree.bst_insert(5)

    # Squared Binary Search Tree
    # binary_tree.bst_insert(1)
    # binary_tree.bst_insert(4)
    # binary_tree.bst_insert(2)
    # binary_tree.bst_insert(3)
    # binary_tree.bst_insert(6)
    # binary_tree.bst_insert(5)

    # Optimal Binary Search Tree
    binary_tree.bst_insert(4)
    binary_tree.bst_insert(2)
    binary_tree.bst_insert(1)
    binary_tree.bst_insert(3)
    binary_tree.bst_insert(5)
    binary_tree.bst_insert(6)

    # print("Height of tree:", binary_tree.height())

    # print("Finding 5 in tree:", binary_tree.find_or_none(5))
    # print("Finding 10 in tree:", binary_tree.find_or_none(10))

    # print("Finding 6 with parent in tree:",
    #       binary_tree.find_with_parent(6).parent.data)

    # print("Pre-order Traversal:")
    # binary_tree.pre_order_traversal(binary_tree.root)

    # print("In-order Traversal:")
    # binary_tree.in_order_traversal(binary_tree.root)

    # print("Post-order Traversal:")
    # binary_tree.post_order_traversal(binary_tree.root)

    binary_tree.print_tree()

    print("=" * 30)
    # Deletion Cases

    # 1- Deleting a leaf node
    print("Deleting 1 (leaf node):")
    binary_tree.bst_delete(1)
    binary_tree.print_tree()

    print("=" * 30)

    # 2- Deleting a node with one child
    print("Deleting 2 (node with one child):")
    binary_tree.bst_delete(2)
    binary_tree.print_tree()

    print("=" * 30)

    # 3- Deleting a node with two children
    print("Deleting 4 (node with two children):")
    binary_tree.bst_delete(4)
    binary_tree.print_tree()
