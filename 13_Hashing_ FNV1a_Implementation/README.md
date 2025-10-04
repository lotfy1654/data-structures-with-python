# Hashing – Introduction & FNV-1a Implementation

**Hashing** is the process of converting data (a key) into a **fixed-size integer value** (called a *hash code* or *hash value*) using a **hash function**.  
This hash value determines the **index** where the data will be stored in a **hash table**.

---

## Hashing Concepts

### 1. What is a Hash?

A **hash** is a *fixed-size numeric value* generated from input data (like a string, number, or file).  
It uniquely represents the input in a compact form.

- The same input → always produces the same hash.  
- Even a tiny change → produces a completely different hash.  

---

### 2. What is a Hash Function?

A **hash function** is a mathematical algorithm that:

- Takes an input (key or data),
- Processes it through specific operations,
- And returns a numeric value (the hash).

---

### 3. What is a Hash Table?

A **Hash Table** (or **Hash Map**) is a data structure that stores *key–value pairs*.  
It uses a hash function to convert a key into an **index** in an internal array, where the value is stored.

**Process:**

1. Key is hashed → produces index  
2. Value is stored at that index  
3. Lookup uses the same hash function to retrieve data quickly  

---

### 4. What is a Map?

A **Map** (also called *Dictionary* or *Associative Array*) is an abstract concept that stores data as pairs:

---

## Hashing Algorithms

Common hash algorithms include:  
**MD5**, **SHA-1**, **FNV-1a**, **NTLM**, **SHA-2**, **SHA-256**, etc.

---

### FNV-1a Algorithm (Steps)

1. Initialize `hash = offset_prime`  
2. For each byte of the data:
   - `hash = hash XOR byte`
   - `hash = hash * FNV_prime`
3. Return the final `hash` value  

## Collision (in Hashing)

A **collision** occurs when **two different keys** produce the **same hash value (index)** after being processed by a hash function.

### Example

```python
  hash("cat") → 15
  hash("dog") → 15
```

Both keys `"cat"` and `"dog"` map to the **same index (15)** in the hash table — this is called a **collision**.

---

### Why Collisions Happen

- The **hash table size** is limited (e.g., only 100 slots).
- The **set of possible keys** is much larger (e.g., millions of strings).
- Even with a good hash function, it’s statistically inevitable that some keys will hash to the same slot.

---

### Collision Handling Techniques

1. **Chaining (Separate Chaining):**  
   - Each slot holds a linked list (or bucket) of all entries that hash to that index.
   - New entries are appended to the list.

2. **Open Addressing:**  
   - If a slot is full, the algorithm searches for another empty slot using a probing method:
     - **Linear Probing:** move sequentially to the next index.
     - **Quadratic Probing:** jump by increasing squares (1², 2², 3²…).
     - **Double Hashing:** use a second hash function to find the next index.

---

### Goal of a Good Hash Function

A good hash function **minimizes collisions** by:

- Distributing keys uniformly across the table.
- Avoiding patterns or clusters.

---

| Term | Meaning | Example |
|------|----------|----------|
| **Collision** | Two keys map to the same index | `"cat"` and `"dog"` → index 15 |
| **Cause** | Limited table size vs. many possible keys | Hash range smaller than key space |
| **Solution** | Chaining or Open Addressing | Linked list or probing |
