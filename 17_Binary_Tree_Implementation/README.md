# Binary Tree – Implementation

A **binary tree** is a hierarchical data structure where each node has at most two children, commonly referred to as the left and right child.

---

## Core Operations

### 1. Insert (Breadth-First)

Breadth-first insertion adds a node at the first available position (left to right).

**Algorithm:**

1. If `root` is `null`:
   - `root = new_node`
   - Return
2. Add `root` to a queue.
3. While the queue is not empty:
   - `current_node = queue.dequeue()`
   - If `current_node.left` is `null`:
     - `current_node.left = new_node`
     - Break
   - Else:
     - `queue.enqueue(current_node.left)`
   - If `current_node.right` is `null`:
     - `current_node.right = new_node`
     - Break
   - Else:
     - `queue.enqueue(current_node.right)`

This ensures that the tree is filled level by level from left to right.

---

### 2. Height of the Tree

The **height** of a tree is the number of nodes along the longest path from the root to a leaf.

**Algorithm (Recursive):**

```python
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

Base case: if the node is None, height is 0.

Recursive step: take the maximum height between left and right subtrees, then add 1 for the current node.

---

### 3. Pre-Order Traversal

**Pre-order traversal** visits nodes in the order:  
**Root → Left → Right**

**Algorithm (Recursive):**

```python
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
```

**Example:**

```python
       1
      / \
     2   3
    / \
   4   5

# Pre-order traversal output:

1, 2, 4, 5, 3
```

---

### 4. In-Order Traversal

**In-order traversal** visits nodes in the order:  
**Left → Root → Right**

**Algorithm (Recursive):**

```python
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)
```

**Example:**

```python
       1
      / \
     2   3
    / \
   4   5

# In-order traversal output:

4, 2, 5, 1, 3
```

---

### 5. Post-Order Traversal

**Post-order traversal** visits nodes in the order:  
**Left → Right → Root**

**Algorithm (Recursive):**

```python
def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=", ")
```

**Example:**

```python
       1
      / \
     2   3
    / \
   4   5

# Post-order traversal output:

4, 5, 2, 3, 1
```
