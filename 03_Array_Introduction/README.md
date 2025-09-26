# Array - Introduction

# 1- Array Addressing – Basic Idea


In a **traditional array** (like in C), all elements are stored in **contiguous memory locations**.  
To access a specific element, we use the formula:

\[
\text{Address}(A[i]) = \text{Base Address}(A) + (i \times \text{Size of each element})
\]

---

## 📌 Explanation

- ✅ **Base Address** = the address of the first element (A[0])  
- ✅ **i** = the index (position of the element)  
- ✅ **Size** = the size of each element (e.g., 4 bytes for an `int`)  

---

## 💡 Example in C

```c
int arr[3] = {10, 20, 30};
// Suppose Base Address = 1000
// Size of int = 4 bytes

Address(arr[0]) = 1000 + (0 * 4) = 1000
Address(arr[1]) = 1000 + (1 * 4) = 1004
Address(arr[2]) = 1000 + (2 * 4) = 1008
```

# 2- Types of Arrays



## 1 ) Regular (One-Dimensional Array)

- A simple **linear collection** of elements.  
- Accessed with a **single index**.  
- Memory is contiguous.  

### Example in Python

```py
arr = [10, 20, 30, 40, 50]
print(arr[2])  # 30
```

### Example in C

```c
int arr[5] = {10, 20, 30, 40, 50};
printf("%d", arr[2]);  // prints 30
```
#
## 2) Two Dimensional Array (2D)

- As table with rows and columns
- Access wth two indices [row , column]
- Memory is stored row by row in C 


### Example
```
      Col0  Col1  Col2
Row0   1     2     3
Row1   4     5     6
```

### Example in Python

```py
arr = [
    [1, 2, 3],
    [4, 5, 6]
]
print(arr[1][2])  # 6
```

### Example in C

```c
int arr[2][3] = { {1,2,3}, {4,5,6} };
printf("%d", arr[1][2]);  // prints 6
```
#
## 3) Three Dimensional Array (3D)
- Can be visualized as a cube (layers of 2D arrays)
- Accessed with three indices [page , row , column]


### Example
```
# Page 1
      Col0  Col1  Col2
Row0   1     2     3
Row1   4     5     6

# Page 2

      Col0  Col1  Col2
Row0   7     8     9
Row1  10    11    12
```

### Example in Python

```py
arr = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print(arr[1][0][2])  # 9
```

### Example in C

```c
int arr[2][2][3] = {
    { {1,2,3}, {4,5,6} },
    { {7,8,9}, {10,11,12} }
};
printf("%d", arr[1][0][2]);  // prints 9
```

#
## 4)  Jagged Array
- Array with different rows lengths
- Memory is not contiguous for all elements

### Example
```
Row0: [1, 2, 3]
Row1: [4, 5]
Row2: [6]
```

### Example in Python

```py
arr = [
    [1, 2, 3],
    [4, 5],
    [6]
]
print(arr[0][2])  # 3
```

### Example in C

```c
int* arr[3];
arr[0] = (int[]){1, 2, 3};
arr[1] = (int[]){4, 5};
arr[2] = (int[]){6};
printf("%d", arr[0][2]);  // prints 3
```
#

## # Array Infrastructure

- The **infrastructure of an array** is the way the array stores data in memory.  
- Arrays are stored in **consecutive (contiguous) memory locations**.  

### Responsibility for Memory Management

| Aspect                  | C Array                                   | Python List                           |
|--------------------------|-------------------------------------------|---------------------------------------|
| **Who decides memory**   | Compiler (at compile-time, fixed size)    | Interpreter (runtime, dynamic)        |
| **Memory layout**        | Contiguous block (low-level)              | References to objects (not contiguous) (high level)|
| **Type system**          | Fixed type (all elements same)            | Can mix types                         |
| **Flexibility**          | Rigid, manual control                     | Flexible, auto-managed                |
