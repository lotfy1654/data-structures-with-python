# Hash Table Implementation

## Core Operations

### 1. Hash

- **Name:** `Hash`
- **Assumptions:** None
- **Inputs:**
  - Key
- **Process:**  
  - hashed_key =offset_basic
  - for each octet_of_data to be hashed
    - hashed_key = hashed_key Xor octet_of_data
    - hashed_key = hashed_key * FNV_prime
  - hashed_key = hashed_key % hashedyable_length
- **Output:**
  - Hashed Key

---

### 2. Collision Handleing

- **Name:** `collision_handling`
- **Assumptions:** None
- **Inputs:**
  - key
  - hash
  - set or get
- **Process:**
  - for i to hash table length - 1
    - new_hash = (hash + i) % hash_table_length `Linear Probling`
  - if set AND (entries[new_hash] is empty OR entries[new_hash].keuy == key)
    - return new_hash
  - else if get AND entries[new_hash].key == key
    - return new_hash
  - else
    - continue
  - new_hash = -1
- **Output:**
  - new_hash  

---

### 3. Add To Entries

- **Name:** `add_to_entries`
- **Assumptions:** None
- **Inputs:**
  - key
  - value
- **Process:**
- index = hash(key , size)
- term = entries[index]
- if entries[index].key not empty AND != key
  - index = collision_handling()
  - item = entries[index]
  - if index == -1 THROW an EXCEPTION
- if entries[index] is empty
  - create new keyValuePair than add it to entries[index]
  - increase entries_count by one
- else if item.key = key
  - update the value
- else
  - THROW an EXCEPTION
- **Output:** None

---

### 4. Resize or not

- **Name:** `resize_or_not`
- **Assumptions:** None
- **Inputs:** None
- **Process:**
  - if entries_count less than entries array's length
    - dont resize and exit
  - else
    - new size = current entries array's length * 2
    - make a copty from the entries array
    - entries_array = new entries array with new size
    - for each entry in entries copy array
      - call `add_to_entries` function
  - delete entries copy array
- **Output:** None

---

### 5. Set

- **Name:** `set`
- **Assumptions:** None
- **Inputs:**
  - key
  - value
- **Process:**
  - call resize_or_not() function
  - call add_to_entries() function
- **Output:** None

---

### 6. Get

- **Name:** `get`
- **Assumptions:** None
- **Inputs:**
  - key
- **Process:**
- index = hash()
- item = entries[index]
- if entries[index] not empty and != key
  - index = collision_handling()
  - if index == -1 return NULL
  - item = entries[key]
- if item.key == key
  - return the value
- else
  - return NULL
- **Output:**
  - Value

---

### 7. Remove

- **Name:** `remove`
- **Assumptions:** None
- **Inputs:**
  - key
- **Process:**
- index = hash()
- item = entries[index]
- if entries[index] not empty and != key
  - index = collision_handling()
  - if index == -1 return NULL
  - item = entries[key]
- if item.key == key
  - value = item.value
  - entries[index] = NULL
  - decrement the entries_count
  - return value
- else
  - return NULL
- **Output:**
  - Value