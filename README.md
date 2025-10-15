# Data Structures in Python

This repository contains educational lessons on **fundamental data structures in Python**, focusing on concepts

## [01_Array_Introduction](./01_Array_Introduction)

- Introduction to Arrays  
- Types of Arrays (1D, 2D, 3D, Jagged)  
- Memory management responsibility in C vs Python  

## [02_Array_Operations_Implementation](./02_Array_Operations_Implementation)

- Implementation of a function to **resize arrays**  
- Implementation of a function to **access elements by index**  `getAt`
- Understanding array operations at a low-level (manual implementation)  

## [03_Linked_List_Introduction_Singly_list_implementation](./03_Linked_List_Introduction_Singly_list_implementation)

- What is a Linked List and how it differs from arrays  
- Types of Linked Lists (Singly, Doubly, Circular)  
- Infrastructure: nodes stored in **independent, non-consecutive memory locations** connected by pointers  
- Singly Linked List basics with diagrams  
- Implementation of core operations:  
  - `insert_last` → insert new node at the end  
  - `insert_after` → insert new node after a given node  
  - `insert_before` → insert new node before a given node  
  - `delete_node` → delete a specific node  

## [04_Linked_List_Doubly_list_implementation](./04_Linked_List_Doubly_list_implementation)

- Introduction to **Doubly Linked List**:  
  A linear data structure where each node stores:  
  - Data  
  - Pointer to the **next** node  
  - Pointer to the **previous** node  

- Supports **bidirectional traversal** (forward & backward).  
- More flexible than singly linked lists because you can efficiently insert/delete from both ends or the middle.

### Core Implementations

- `insert_last` → Insert at the end  
- `insert_after` → Insert after a given node  
- `insert_before` → Insert before a given node  
- `delete_node` → Remove a node from the list  
- `copy` → Create an independent copy of the list  

## [05_Linked_List_VS_Array](./05_Linked_List_VS_Array)

### Arrays

- Stored in **contiguous memory locations**.  
- **Random access** is very fast → `O(1)`.  
- **Insertion/Deletion** is costly → `O(n)` (needs shifting elements).  
- **Fixed size** (needs resizing if full).  
- **Memory efficient** (no extra storage for pointers).  
- Better **cache locality** → faster iteration.

### Linked Lists

- Stored in **non-contiguous memory locations** (nodes linked with pointers).  
- **Access by index** is slow → `O(n)` (must traverse from head).  
- **Insertion/Deletion** is efficient (especially at beginning/middle).  
- **Dynamic size** → grows/shrinks as needed.  
- Extra **memory overhead** (needs pointers in each node).  
- Poorer cache locality compared to arrays.

### Quick Comparison

| Feature              | Array             | Linked List        |
|----------------------|------------------|--------------------|
| Memory Allocation    | Contiguous       | Non-contiguous     |
| Access (by index)    | `O(1)`           | `O(n)`             |
| Insertion/Deletion   | `O(n)`           | `O(1)` (if node known) |
| Size                 | Fixed/Resizable  | Dynamic            |
| Memory Overhead      | Low              | High (pointers)    |
| Cache Performance    | Good             | Poor               |

- **Use Arrays** when you need **fast access & cache efficiency**.  
- **Use Linked Lists** when you need **frequent dynamic insertions/deletions**.

## [06_Stack_Introduction](./06_Stack_Introduction)

A **stack** is a linear data structure that follows **LIFO** (Last In, First Out).  
The last element added (`pushed`) is the first one removed (`popped`).  

Stacks can be implemented using:

- **Arrays** (fixed size, may require resizing, supports fast access)
- **Linked Lists** (dynamic size, flexible insertions/deletions)

Core operations include:

- `push(x)` → add element to the top  
- `pop()` → remove and return top element  
- `peek()` / `top()` → view top element without removing  
- `isEmpty()` → check if stack is empty  
- `isFull()` → check if stack is full (for arrays)  
- `size()` → current number of elements

## [07_Linked_List_based_Stack](./07_Linked_List_based_Stack)

Implementation of a `stack using a linked list`

## [08_Array_based_Stack](./08_Array_based_Stack)

Implementation of a `stack using an array` (Python list)

## [09_Queue_Introduction](./09_Queue_Introduction)

A **queue** is a linear data structure that follows **FIFO** (First In, First Out).  
The first element added (`enqueued`) is the first one removed (`dequeued`).  

Queues can be implemented using:

- **Arrays** (fixed size, may require resizing, supports fast access)  
- **Linked Lists** (dynamic size, flexible insertions/deletions)  

Core operations include:

- `enqueue(x)` → add element to the rear (end)  
- `dequeue()` → remove and return element from the front (beginning)  
- `peek()` / `front()` → view front element without removing  
- `isEmpty()` → check if queue is empty  
- `isFull()` → check if queue is full (for arrays)  
- `size()` → current number of elements

## [10_Linked_List_based_Queue](./10_Linked_List_based_Queue)

Implementation of a `queue using a linked list`

## [11_Array_based_Queue](./11_Array_based_Queue)

Implementation of a `queue using an array` (Python list)

## [12_KeyValuePair_Dictionary_Implementation](./12_KeyValuePair_Dictionary_Implementation)

- **Key–Value Pair**: a pair of `key` and `value`, where **key is unique** and maps to a value.  
- **Dictionary / Map**: a collection of Key–Value Pairs.  
- Usually implemented using **Hash Table** for fast access.  
- Core operations: `set()`, `get()`, `delete()`, `resize()`, `size()`  

## [13_Hashing_FNV1a_Implementation](./13_Hashing_%20FNV1a_Implementation)

- **Hashing**: process of mapping data to a fixed-size value (hash code) for fast lookup.  
- **Hash Function**: function that converts a key into a hash code (index in a hash table).  
- **Hash Table / Map**: data structure that stores Key–Value Pairs using a hash function for fast operations.  
- Implementation example: **FNV-1a hash function** for both 32-bit and 64-bit hashes

## [14_HashTable_Introduction](./14_HashTable_Introduction)

- **Hash Table (Hash Map):** A data structure that stores **key–value pairs** and provides **fast insertion, deletion, and lookup** using keys.  
- **Hash Function:** Converts a **key** into an **array index** where the value is stored.  
- **Collision:** Occurs when two keys produce the same index — must be handled properly.  
- **Core Operations:**  
  1. Convert key to array index.  
  2. Handle collisions efficiently.  

### Collision Resolution Techniques

| Technique | Type | Main Idea | Example Formula |
|-----------|------|------------|----------------|
| **Linear Probing** | Open Addressing | Try the next slot sequentially | `(hash + i) % n` |
| **Quadratic Probing** | Open Addressing | Jump by squares of i (1, 4, 9, …) | `(hash + pow(i, 2)) % n` |
| **Double Hashing** | Open Addressing | Use a second hash function for step size | `(hash1 + i * hash2) % n` |
| **Separate Chaining** | Closed Hashing | Store multiple keys in a list at same index | `table[index].append(key, value)` |

### Key Concepts

- **Open Addressing:** All data stored inside the table; probe for next slot when collision occurs.  
- **Closed Hashing (Separate Chaining):** Each slot holds a collection (like a linked list) to store multiple items that hash to the same index.  
- **Goal:** Maintain **O(1)** average time for insertion, deletion, and search operations.  

## [15_Hash_Table_Implementation](./15_Hash_Table_Implementation)

Implementation of a `hash table`

Core operations include:

- `hash(key)` → compute the hash index  
- `collision_handling(key, hash, mode)` → find a valid index when a collision occurs using Linear Probing
- `set(key, value)` → insert or update a key-value pair  
- `get(key)` → retrieve the value by key  
- `remove(key)` → delete a key-value pair  
- `resize()` → expand the table when full  

## [16_Binary_Tree_Introduction](./16_Binary_Tree_Introduction)

Introduction to the **Binary Tree** — a hierarchical data structure where each node has at most two children: `left` and `right`.

Core concepts include:

- **Structure:** Each node has up to two children (left and right).  
- **Key Terms:** Root, Node, Edge, Leaf, Height, Depth, and Subtree.  
- **Traversals:**  
  - Depth-First → Pre-order, In-order, Post-order  
  - Breadth-First → Level-order  

Core operations include:

- `insert(node)` → add a new node (breadth-first or BST-based)  
- `delete(node)` → remove a node and maintain structure  
- `search(value)` → find a node with a given key or value  
- `traverse(order)` → visit nodes (pre, in, post, or level order)  
- `height(node)` → compute height of the tree  
- `min_value()` / `max_value()` → find minimum or maximum (in BST)  

## [17_Binary_Tree_Implementation](./17_Binary_Tree_Implementation)

Implementation of a **Binary Tree** using a **Queue (Linked List–based)**.

Includes:

- Linked List–based `Queue` for breadth-first insertion  
- `BinaryTree` class with:
  - `insert(data)` → level-order insertion  
  - `height(node)` → recursive height calculation  
  - `pre_order`, `in_order`, `post_order` traversals  

## [18_Binary_Search_Tree](./18_Binary_Search_Tree)

A **Binary Search Tree (BST)** is a type of **binary tree** that keeps elements in **sorted order**, allowing efficient **search**, **insertion**, and **deletion**.

- **Left subtree** → contains values **less than** the node  
- **Right subtree** → contains values **greater than** the node  
- Both subtrees are also **Binary Search Trees**

This structure provides an **average-case time complexity of O(log n)** for core operations.

Core operations include:

- `insert(data)` → add a new node while maintaining the BST property  
- `find(data)` → search for a node by its value  
- `delete(data)` → remove a node (handle leaf, one-child, or two-child cases)  
- `balance()` → rebuild the tree into a height-balanced structure  

## [19_Heap_Tree](./19_Heap_Tree)

A **Heap Tree** is a **complete binary tree** that satisfies the **heap property** — every parent node is ordered with respect to its children.

- In a **Max Heap**, each parent’s value is **greater than or equal** to its children.  
- In a **Min Heap**, each parent’s value is **less than or equal** to its children.  

This structure allows **fast access** to the highest or lowest value and is widely used in **priority queues** and **heap sort**.

Core operations include:

- `insert(x)` → add a new element and restore heap property  
- `extract_min()` / `extract_max()` → remove and return the root element  
- `peek()` → return the root without removing it  
- `heapify()` → build a heap from an array  

## [20_Priority_Queue](./20_Priority_Queue)

A **Priority Queue** is a **special type of queue** where each element has a **priority**.  
Unlike a normal queue (FIFO – *First In, First Out*), elements are **served based on their priority** rather than arrival order.

- The element with the **highest** or **lowest** priority is processed **first**.  
- If two elements share the same priority, the one inserted **earlier** is served first (FIFO rule).

Core operations include:

- `enqueue(priority, data)` → insert a new element based on priority  
- `dequeue()` → remove and return the highest/lowest priority element  
- `peek()` → view the next element without removing it  
- `isEmpty()` → check if the queue is empty  

Priority queues are commonly implemented using a **Binary Heap** for efficient operations:

| Implementation | Insert | Remove | Peek |
|----------------|---------|---------|------|
| **Binary Heap** | O(log n) | O(log n) | O(1) |

Two main types:

- **Min-Priority Queue** → smallest priority value served first  
- **Max-Priority Queue** → largest priority value served first  
