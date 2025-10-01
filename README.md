# Data Structures in Python

This repository contains educational lessons on **fundamental data structures in Python**, focusing on concepts

## 01_Array_Introduction

- Introduction to Arrays  
- Types of Arrays (1D, 2D, 3D, Jagged)  
- Memory management responsibility in C vs Python  

## 02_Array_Operations_Implementation

- Implementation of a function to **resize arrays**  
- Implementation of a function to **access elements by index**  `getAt`
- Understanding array operations at a low-level (manual implementation)  

## 03_Linked List_Introduction_Singly_list_implementation

- What is a Linked List and how it differs from arrays  
- Types of Linked Lists (Singly, Doubly, Circular)  
- Infrastructure: nodes stored in **independent, non-consecutive memory locations** connected by pointers  
- Singly Linked List basics with diagrams  
- Implementation of core operations:  
  - `insert_last` → insert new node at the end  
  - `insert_after` → insert new node after a given node  
  - `insert_before` → insert new node before a given node  
  - `delete_node` → delete a specific node  

## 04_Linked_List_Doubly_list_implementation

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

## 05_Linked_List_VS_Array

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