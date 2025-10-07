# Binary Tree – Introduction

## What is a Binary Tree?

A **Binary Tree** is a hierarchical **tree data structure** where each node has at most **two children**:  

- **Left child**  
- **Right child**  

Binary trees are typically stored in **non-contiguous memory**, meaning nodes are **not stored sequentially in an array**.

The topmost node is called the **root**.  
Nodes with no children are called **leaf nodes**.

![Binar](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/450px-Binary_search_tree.svg.png?20090116232809)

---

### Key Terms

| Term       | Definition |
|------------|------------|
| Root       | Topmost node of the tree |
| Node       | Individual element of the tree |
| Edge       | Connection between parent and child nodes |
| Leaf       | Node with no children |
| Height     | Length of the longest path from root to a leaf |
| Depth      | Length of path from root to a particular node |
| Subtree    | A tree formed by any node and its descendants |

---

## Types of Binary Trees

1. **Full Binary Tree**  
   - Every node has **0 or 2 children**.  

2. **Perfect Binary Tree**  
   - All internal nodes have 2 children, and all **leaves are at the same level**.  

3. **Complete Binary Tree**  
   - All levels are fully filled except possibly the last, which is filled **from left to right**.  

4. **Balanced Binary Tree**  
   - Height difference between left and right subtree of any node is ≤ 1.  

5. **Degenerate (or Pathological) Tree**  
   - Every parent node has **only one child**, behaves like a linked list.  

---

## Binary Tree Traversals

### 1. Depth-First Traversals (DFS)

| Type          | Order of visiting nodes |
|---------------|-----------------------|
| **Pre-order** | Root → Left → Right |
| **In-order**  | Left → Root → Right |
| **Post-order**| Left → Right → Root |

### 2. Breadth-First Traversal (BFS)

- Also called **Level-order Traversal**  
- Visit nodes **level by level** from top to bottom, left to right.  

---

## Core Operations

| Operation      | Description |
|----------------|------------|
| **Insert**     | Add a node at a specific position based on tree type |
| **Delete**     | Remove a node and reorganize tree to maintain properties |
| **Search/Find**     | Find a node with a specific value |
| **Traversal**  | Visit all nodes in a specific order (pre/in/post/level) |
| **Height**     | Compute the height of the tree |
| **Minimum/Maximum** | Find min/max value in the tree (for BSTs) |

---

## Binary Search Tree (BST) Special Case

- A **BST** is a binary tree with the property:  
  - **Left child < Parent < Right child**  
- Allows **fast search, insert, and delete** in average time **O(log n)**.  

---

## Example (Tree Structure)

```python
    10
   /  \
  5    15
 / \   / \
2   7 12 20
```

- Pre-order: 10, 5, 2, 7, 15, 12, 20  
- In-order: 2, 5, 7, 10, 12, 15, 20  
- Post-order: 2, 7, 5, 12, 20, 15, 10  
- Level-order: 10, 5, 15, 2, 7, 12, 20  

---
