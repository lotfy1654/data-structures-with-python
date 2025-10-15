# Priority Queue

## What is a Priority Queue?

A **Priority Queue** is a **special type of queue** where **each element is associated with a priority**.  
Unlike a normal queue (FIFO – *First In, First Out*),  
elements are **served based on their priority**, not their order of arrival.

> The element with the **highest (or lowest)** priority is processed **first**.


---

## Characteristics

- Every element has two parts:
  1. **Value (Data)**
  2. **Priority (Key)**
- The **priority** determines the **order of removal**.
- If two elements have the same priority:
  - The **order of insertion** (FIFO) decides which one goes first.

---

## Example

| Element | Priority |
|----------|-----------|
| A | 2 |
| B | 1 |
| C | 3 |

If this is a **max-priority queue**, removal order is:  
`C → A → B`

If this is a **min-priority queue**, removal order is:  
`B → A → C`

---

## Implementation

| Implementation | Description | Time Complexities |
|----------------|--------------|-------------------|
| **Unsorted Array / List** | Insert at end; find highest priority element on removal. | Insert: O(1) <br> Remove: O(n) |
| **Sorted Array / List** | Keep array sorted by priority. | Insert: O(n) <br> Remove: O(1) |
| **Binary Heap (Recommended)** | Maintain heap property for fast access to min/max element. | Insert: O(log n) <br> Remove: O(log n) <br> Peek: O(1) |

> The **heap-based implementation** is the most efficient and commonly used method.

---

## Core Operations

| Operation | Description | Time Complexity |
|------------|--------------|-----------------|
| **Insert / Enqueue (push)** | Add a new element with a priority. | O(log n) |
| **Remove / Dequeue (pop)** | Remove the element with the highest (or lowest) priority. | O(log n) |
| **Peek / Top** | View the element with highest (or lowest) priority without removing it. | O(1) |
| **isEmpty** | Check if the queue is empty. | O(1) |

---

## Types of Priority Queues

1. **Min-Priority Queue**
   - The **element with the smallest priority value** is removed first.
   - Backed by a **Min-Heap**.

2. **Max-Priority Queue**
   - The **element with the largest priority value** is removed first.
   - Backed by a **Max-Heap**.
