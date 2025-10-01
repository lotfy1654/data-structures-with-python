# Arrays vs Linked Lists — Comprehensive Comparison

---

## When to Use Arrays vs Linked Lists

| Criteria                  | Use Arrays When...                                                                      | Use Linked Lists When...                                                                   |
|----------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Memory Allocation**      | Memory needs to be allocated in a **contiguous block**.                                 | Memory can be allocated **dynamically and non-contiguously**.                              |
| **Access Speed**           | Fast access to elements by **index** is required (**O(1)** access).                      | Access speed is not the primary concern, and traversal is acceptable.                      |
| **Size of Data Structure** | The size of the data structure is **fixed or known in advance**.                         | The size of the data structure is **dynamic or frequently changing**.                      |
| **Insertion/Deletion**     | Insertions and deletions are **infrequent** and mostly at the **end**.                   | Frequent insertions and deletions are needed, especially at the **beginning or middle**.   |
| **Memory Efficiency**      | Memory efficiency is important, and **overhead from pointers should be minimized**.      | Slightly higher memory usage is acceptable due to the **overhead of pointers**.            |
| **Implementation**         | **Simplicity** and ease of implementation are priorities.                                | **Flexibility** and dynamic memory management are priorities.                              |
| **Cache Performance**      | Cache performance is critical → data should be stored **contiguously**.                  | Cache performance is less critical, and non-contiguous storage is acceptable.              |
| **Sorting & Searching**    | Frequent sorting/searching (esp. **binary search O(log n)**) is required.                | Sorting/searching are less common or handled differently.                                  |
| **Fixed Data Types**       | Collection of elements of the **same type** is needed.                                   | Nodes can store **different types** or **complex objects**.                                |
| **Real-Time Systems**      | Needs to support **real-time access and processing**.                                    | Real-time access is less critical, **flexibility** is more important.                      |

---

## When to Choose Which?

- Use **Array (list)** when:
  - You need **fast random access** (`arr[i]`).
  - **Memory locality** and **iteration speed** matter.
  - Insertions/deletions are **mostly at the end** (append/pop).

- Use **Singly Linked List** when:
  - You need **many inserts/deletes** at the beginning or middle.
  - You already have references to nodes.
  - You **don’t need random access** by index.

- Use **Doubly Linked List** when:
  - You need **deletion from the tail in O(1)** or **bidirectional traversal**.
  - You can accept **extra memory overhead** for `prev` pointers.

---

## Array vs Linked List: Time Complexity

| Operation               | Array (Time Complexity)            | Linked List (Time Complexity)  |
|--------------------------|------------------------------------|--------------------------------|
| **Access (by Index)**    | O(1)                               | O(n)                           |
| **Search (Unsorted)**    | O(n)                               | O(n)                           |
| **Search (Sorted)**      | O(log n) with Binary Search        | O(n)                           |
| **Insertion (Beginning)**| O(n)                               | O(1)                           |
| **Insertion (End)**      | O(1) (if space available)          | O(1) (with tail pointer)       |
| **Insertion (Middle)**   | O(n)                               | O(n)                           |
| **Deletion (Beginning)** | O(n)                               | O(1)                           |
| **Deletion (End)**       | O(1) (if space available)          | O(1) (with tail pointer)       |
| **Deletion (Middle)**    | O(n)                               | O(n)                           |

---

## Array vs Linked List: Space Complexity

| Aspect                | Array Space Complexity                                 | Linked List Space Complexity                                         |
|-----------------------|---------------------------------------------------------|----------------------------------------------------------------------|
| **Storage of Elements** | **O(n)** – Stores `n` elements directly                | **O(n)** – Stores `n` elements directly                              |
| **Memory Overhead**   | None – only the data is stored                          | **O(n)** extra for pointers (`next` / `prev` in case of doubly linked list) |
| **Dynamic Sizing**    | Fixed size (must allocate in advance). Resizing requires creating a new array. | Dynamic size – can grow/shrink easily with insertions/deletions.     |
| **Efficiency**        | More memory-efficient without pointer overhead          | Less memory-efficient due to additional pointer storage.             |

---

## Difference Between Array and Linked List: Comparison

| **Aspect**             | **Array**                                                                 | **Linked List**                                                                           |
|-------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Definition**          | A collection of elements stored in a contiguous block of memory.          | A collection of nodes linked by pointers, stored non-contiguously.                        |
| **Memory Allocation**   | Contiguous memory block.                                                  | Non-contiguous memory; each element stored in a node with a pointer.                       |
| **Types**               | One-dimensional, multi-dimensional (2D, 3D arrays).                       | Singly Linked List, Doubly Linked List, Circular Linked List.                              |
| **Access**              | **O(1)** – Direct access by index.                                        | **O(n)** – Traversal needed to access elements.                                           |
| **Search**              | **O(n)** for unsorted, **O(log n)** for sorted (binary search).           | **O(n)** – Linear search required.                                                        |
| **Insertion (Beginning)**| **O(n)** – All elements must be shifted.                                 | **O(1)** – Direct insertion without shifting.                                             |
| **Insertion (End)**     | **O(1)** if space available, **O(n)** if resizing is needed.              | **O(1)** with tail pointer, **O(n)** without tail pointer.                                 |
| **Insertion (Middle)**  | **O(n)** – Elements must be shifted.                                      | **O(n)** – Traversal required to find insertion point.                                     |
| **Deletion (Beginning)**| **O(n)** – All elements must be shifted.                                 | **O(1)** – Direct removal of the first node.                                              |
| **Deletion (End)**      | **O(1)** if space available, **O(n)** if resizing is required.            | **O(1)** with tail pointer, **O(n)** without tail pointer.                                 |
| **Deletion (Middle)**   | **O(n)** – Elements must be shifted.                                      | **O(n)** – Traversal required to find and remove the node.                                 |
| **Dynamic Resizing**    | Not flexible – Fixed size, resizing requires new memory allocation.       | Flexible – Grows and shrinks dynamically as needed.                                        |
| **Memory Overhead**     | Efficient – Only stores elements.                                         | Higher – Each node requires extra memory for pointers.                                     |
| **Cache Performance**   | Better – Contiguous allocation improves cache locality.                   | Worse – Non-contiguous allocation reduces cache efficiency.                                |
| **Space Complexity**    | **O(n)** – Space allocated for n elements.                                | **O(n) + O(n)** for pointers – Extra space needed for pointers in each node.              |
| **Implementation**      | Simple to implement and manage.                                          | More complex due to pointer management and dynamic memory.                                 |
| **Best Use Cases**      | - Quick element access needed.<br>- Number of elements is fixed.<br>- Static storage like tables/matrices. | - Frequent insertions/deletions.<br>- Dynamic memory size needed.<br>- Queues, history management. |
| **Drawbacks**           | - Fixed size, costly resizing.<br>- Costly insert/delete due to shifting. | - Slower access time.<br>- Extra memory overhead for pointers.                             |
| **Example Applications**| Static data storage, tables, matrices.                                    | Dynamic memory allocation, queues, browser history.                                        |