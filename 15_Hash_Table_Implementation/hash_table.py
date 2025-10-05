# Implementation of Hash Table with FNV-1a Hash Function
class HashTable:
    def __init__(self):
        self.initial_size = 3
        self.entries_count = 0
        self.entries = [None] * self.initial_size

    # FNV-1a 32-bit hash functions
    def hash(self, data):
        # FNV-1a 32-bit parameters
        offset_prime = 2166136261
        fnv_prime = 16777619

        # Convert string to bytes
        data_bytes = data.encode('ascii')

        # Initialize hash value to offset basis
        hash_value = offset_prime

        # Perform FNV-1a hashing
        for i in range(len(data_bytes)):
            # XOR the byte into the least significant byte of the hash
            hash_value = hash_value ^ data_bytes[i]
            # force 32-bit
            # & 0xffffffff => use bitwise AND to limit to 32 bits every (f) is 4 bits so 8 f's equals 32 bits 4*8=32 bits
            hash_value = (hash_value * fnv_prime) & 0xffffffff  # force 32-bit

        print(data + " <- hashed 32 to -> " +
              str(hash_value) + " hex value: " + hex(hash_value))

        # Ensure 32-bit output
        return hash_value % len(self.entries)

    # Collision handling using linear probing
    def collision_handling(self, key, hash, set):
        # set = True for set operation, False for get/remove operation
        for i in range(1, len(self.entries)):
            # Linear probing: try the next slot
            new_hash = (hash + i) % len(self.entries)
            print("[coll] " + str(key) + " " + str(hash) + ", new hash: " +
                  str(new_hash))
            # If setting, find an empty slot or the same key
            if (set and (self.entries[new_hash] is None or self.entries[new_hash].key == key)):
                return new_hash
            # If getting/removing, find the same key
            elif not set and self.entries[new_hash] and self.entries[new_hash].key == key:
                return new_hash
        return -1

    # Add key-value pair to entries
    def add_to_entries(self, key, value):
        # Calculate hash for the key
        hash = self.hash(key)
        # If collision occurs, handle it using collision handling by if entry is not None and keys are different
        if self.entries[hash] is not None and self.entries[hash].key != key:
            hash = self.collision_handling(key, hash, True)

        # If no suitable slot found, raise an exception
        if hash == -1:
            raise Exception(
                "Could not find a place to store the key-value pair")

        # If the slot is empty, add the new key-value pair
        if self.entries[hash] is None:
            # Create a new KeyValuePair and add it to the entries
            new_pair = KeyValuePair(key, value)
            # Add the new pair to the entries
            self.entries[hash] = new_pair
            self.entries_count += 1
        # If the key already exists, update its value
        elif self.entries[hash].key == key:
            self.entries[hash].value = value
        # If the key is not found, raise an exception
        else:
            raise Exception("Could not add the key-value pair")

    # Resize the hash table if the load factor exceeds 1
    def resize_or_not(self):
        # if entries count is less than the length of entries, do nothing
        if self.entries_count < len(self.entries):
            return
        # else double the size of the entries and rehash all existing entries
        else:
            # Double the size of the entries
            new_size = len(self.entries) * 2
            # Create a new list of entries with the new size
            new_entries = [None] * new_size
            # Rehash all existing entries and add them to the new list
            entries_copy = self.entries.copy()
            # Assign the new list to the entries
            self.entries = new_entries
            # Reset the entries count
            self.entries_count = 0
            # Re-add all existing entries to the new list
            for i in range(len(entries_copy)):
                if entries_copy[i] is None:
                    continue
                # Re-add the entry to the new list
                self.add_to_entries(entries_copy[i].key, entries_copy[i].value)

    # Set key-value pair in the hash table
    def set(self, key, value):
        self.resize_or_not()
        self.add_to_entries(key, value)

    # Get value by key from the hash table
    def get(self, key):
        # Calculate hash for the key
        hash = self.hash(key)
        # If collision occurs, handle it using collision handling
        if self.entries[hash] is None or self.entries[hash].key != key:
            hash = self.collision_handling(key, hash, False)

        # If no suitable slot found, return None
        if hash == -1 or self.entries[hash] is None:
            return None

        # If the key is found, return its value
        if self.entries[hash].key == key:
            return self.entries[hash].value
        # else raise an exception
        else:
            raise Exception("Could not find the value for the key")

    # Remove key-value pair from the hash table
    def remove(self, key):
        hash = self.hash(key)
        if self.entries[hash] is None or self.entries[hash].key != key:
            hash = self.collision_handling(key, hash, False)

        if hash == -1 or self.entries[hash] is None:
            return None

        # If the key is found, remove it and return its value
        if self.entries[hash].key == key:
            # Store the value to return later
            value = self.entries[hash].value
            # Remove the entry by setting it to None
            self.entries[hash] = None
            # Decrement the entries count
            self.entries_count -= 1
            return value
        else:
            raise Exception("Could not find the value for the key")

    # Print all entries in the hash table
    def print_entries(self):
        for i in range(len(self.entries)):
            if self.entries[i] is not None:
                print(
                    f"[{i}] -> Key: {self.entries[i].key}, Value: {self.entries[i].value}")

    # Return the number of entries in the dictionary
    def size(self):
        return self.entries_count

    def print(self):
        # Print separator and table size
        print("-----------")
        # Loop through all the entries in the hash table
        for i in range(len(self.entries)):
            if self.entries[i] is None:
                # If the entry is empty, print its index and 'null'
                print("[" + str(i) + "] null")
            else:
                # If the entry is not empty, print its index, Key, and value
                print("[" + str(i) + "] " + self.entries[i].key + ":" +
                      self.entries[i].value)
        # Print separator
        print("-----------")

# Key-Value Pair Class for storing entries in the hash table


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.print_entries()
    hash_table.set("name", "John")
    hash_table.set("age", "30")
    hash_table.set("city", "New York")
    hash_table.print()
    print("Get name:", hash_table.get("name"))
    print("Get age:", hash_table.get("age"))
    hash_table.print()
    hash_table.set("name", "Jane")
    hash_table.print()
    print("Remove age:", hash_table.remove("age"))
    hash_table.print()
