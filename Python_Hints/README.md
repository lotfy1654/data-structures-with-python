# Python Hints: Private Variables & Name Mangling & Garbage Collection (GC)

## Private Variables & Name Mangling

### Private Variables

- In Python, a single underscore (`_var`) is a **convention** to indicate that a variable is intended for internal use only.  
- A double underscore (`__var`) triggers **Name Mangling**, making the variable harder to access from outside the class.  

### What is Name Mangling?

- **Definition**:  
  Name Mangling is a mechanism in Python that automatically changes the name of variables that start with double underscores (`__var`).  
  This helps avoid conflicts and enforces encapsulation.  

- **How it works**:  

  ```python
  class MyClass:
      def __init__(self):
          self.__secret = 42

  obj = MyClass()
  # Internally, __secret is renamed to _MyClass__secret
  print(obj._MyClass__secret)   # 42


---

## Garbage Collection in Python

### What is Garbage Collection?

- Garbage Collection (GC) is the process of **automatically managing memory** in Python.  
- It frees memory that is no longer in use, so developers don’t have to manually deallocate memory (like in C/C++).  
- In Python, you don’t always need to use `del` manually, because the **Garbage Collector** will automatically remove objects when no references exist.  

### How it works

### 1. Reference Counting
- Python keeps track of how many references point to an object.  
- When the reference count drops to `0`, the object is immediately destroyed.  

```python
import sys  

a = [1, 2, 3]
print(sys.getrefcount(a))  # Shows how many references exist to 'a'
```

### Cycle Detection

- Python also has a **cyclic garbage collector** to handle reference cycles (when objects reference each other).  
- This ensures that even if two or more objects reference each other, but no external references exist, they can still be cleaned up.  

```python
import gc    

class Node:
    def __init__(self):
        self.ref = None  

a = Node()
b = Node()

# Creating a cycle
a.ref = b
b.ref = a  

# Removing external references
del a
del b  

# Even though a and b reference each other, 
# GC can collect them since no external reference exists
gc.collect()
```

If we remove both external references:

```python
del a
del b
```
The objects are still in memory because each one holds a reference to the other

#### Why Reference Counting Alone Is Not Enough

### Reference Counting
Python primarily uses **reference counting** for memory management:

- Each object keeps track of how many references point to it.
- When the reference count reaches **zero** → the object is destroyed immediately.

---

#### The Problem: Cycles
Consider the following situation:

- `a` references `b`
- `b` references `a`

This creates a **cycle**.  
Even if there are no external references to either `a` or `b`, their reference counts will **never reach zero**, because they keep each other alive.

So they remain in memory, even though the program can no longer reach them.

---

### Solution: Cyclic Garbage Collector
Python includes a **Cyclic Garbage Collector** in addition to reference counting:

- It runs **periodically** in the background.
- It scans memory for groups of objects that **only reference each other** and have no external references.
- These objects are marked as **unreachable**.
- Python then safely deletes them, breaking the cycle and freeing memory.

---

## Summary
- **Reference Counting** works for most cases but fails with cycles.
- **Cyclic Garbage Collector** solves the cycle problem by detecting unreachable objects.
- Together, they ensure efficient memory management in Python.

