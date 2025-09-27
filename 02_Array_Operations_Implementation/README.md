# Array – Operations Implementation 

## Function Resize

### Name 
- Resize


### Assumptions

- array data is stored in memeory heap
- array address is stored in memory stack


### Inputs

- The array data type 
- the array itself
- new size


### Processes

#### Validations
- the new size is a valid number 
- the array is not null
- the new size is not equal the current size

#### resize
- create new empty array from the same typer with the new size 
- move all items from source array to the new array 
- assign the address of the new array for the source array address


### Outputs

- nothing


## Function Get At

### Name
- getAt


### Assumptions

- array data is stored in memeory heap
- array address is stored in memory stack


### Inputs

- The array data type 
- the array itself
- index

### Processes

#### Validations
- index is 0 or greater

- get item 
  - get the memory address of the 0th item
  - get the size of the data type of the array 
  - calculate the address of the given index
  - get value from memory using the calcilated address


### Outputs
- Single item or default value

#


## `ctypes`
    - The ctypes library in Python allows you to work with C-compatible data types (like int, char, double) and use them as if you were programming in C
    - It provides low-level access to memory and pointers

## `ctypes.c_int`

    - This is a data type provided by the `ctypes` library in Python
    - It represents the `int` type in C
    - By default, it is a 32-bit signed integer (usually 4 bytes)

## `ctypes.POINTER(ctypes.c_int)`
    - Instead of holding the value itself (ctypes.c_int), it holds the memory address of that value

## `ctypes.memmove`

    - ctypes.memmove is a function in the ctypes library
    - It copies a block of memory from a source address to a destination address 
    - Equivalent to the C function memmove() from <string.h> 
    - Useful when working with raw memory, arrays, or when resizing/moving data 

```python
ctypes.memmove(destination, source, size_in_bytes)
```

#

# Resizing Arrays in Python vs C

- Python is **not a low-level language** like C 
- There is **no direct control over raw memory addresses** in the same way as in C 

---

### In C
- You can use functions like `malloc` and `realloc` to allocate or resize memory 
- Sometimes, `realloc` can **resize the same memory block in-place** without copying 

---

### In Python (even with `ctypes`)
- There is **no true in-place resize** for arrays 
- Resizing is always:  
  1. Allocate a **new block of memory** 
  2. **Copy** the old data into the new block 
  3. Return the new block (array) 
- The **old block** stays in memory until Python’s **Garbage Collector (GC)** removes it (if no references remain) 

---

### Important Note
This is exactly how Python’s built-in `list` works under the hood:  
- When you append beyond capacity, Python allocates a larger memory block and copies the old elements into it 
- The resizing happens **automatically** and is hidden from you 

---

**Summary:**  
In Python, **resizing an array = new allocation + copy**, never in-place 
Only in C (with `realloc`) you *might* get true in-place resizing 
