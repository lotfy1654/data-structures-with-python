# Key-Value Pair Dictionary Implementation

# Define a simple Key-Value Pair class
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Define a simple Dictionary class using Key-Value Pairs
class SimpleDictionary:
    # Define constructor
    def __init__(self, initial_size=3):
        # Initialize the dictionary with a fixed-size array
        self.initial_size = initial_size
        # Create an array of KeyValuePair objects or None if empty Size is equal to initial_size
        self.entries = [None] * self.initial_size
        # Initialize the count of entries
        self.entries_count = 0

    # Method To Resize the entries array if needed
    def resize_or_not(self):
        # Check if resizing is needed or not
        # If entries_count is less than the length of entries array - 1, don't resize
        if self.entries_count < len(self.entries) - 1:
            # Don't resize
            return
        else:
            # Create new size
            new_size = len(self.entries) + self.initial_size
            # Create new entries array with new size
            new_entries = [None] * new_size
            # Copy old entries to new entries array
            for i in range(self.entries_count):
                new_entries[i] = self.entries[i]
            # Update entries to new entries array
            self.entries = new_entries
            print(
                f"Resized from: {self.initial_size} -> to new size: {new_size}")

    # Method to set a key-value pair to the dictionary
    def set(self, key, value):
        # Check if key already exists, if so update the value
        for i in range(self.entries_count):
            if self.entries[i].key == key:
                self.entries[i].value = value
                return

        # Key does not exist, add new key-value pair
        # Resize if needed
        self.resize_or_not()
        # Add new key-value pair
        new_pair = KeyValuePair(key, value)
        # Add new entry to the entries array at the current count index
        self.entries[self.entries_count] = new_pair
        self.entries_count += 1

    # Method to get the value for a given key
    def get(self, key):
        # Search for the key in the entries array
        for i in range(self.entries_count):
            if self.entries[i].key == key:
                return self.entries[i].value
        # If key not found, return a default message
        return "Key not found"

    # Method to delete a key-value pair from the dictionary
    def delete(self, key):
        # Search for the key in the entries array
        for i in range(self.entries_count):
            # If key found and entry is not None, delete it by replacing it with the last entry
            if self.entries[i] is not None and self.entries[i].key == key:
                # Replace the entry to be deleted with the last entry
                self.entries[i] = self.entries[self.entries_count - 1]
                # Set the last entry to None and decrease the count
                self.entries[self.entries_count - 1] = None
                # Decrease the count of entries
                self.entries_count -= 1

    def print_entries(self):
        for i in range(self.entries_count):
            if self.entries[i] is not None:
                print(
                    f"[{i}] -> Key: {self.entries[i].key}, Value: {self.entries[i].value}")

    # Return the number of entries in the dictionary
    def size(self):
        return self.entries_count


if __name__ == "__main__":
    dictionary = SimpleDictionary()
    dictionary.set("name", "Alice")
    dictionary.set("age", 30)
    dictionary.print_entries()
    dictionary.set("city", "New York")
    dictionary.print_entries()

    print('Key "name":', dictionary.get("name"))

    print('Dictionary Size:', dictionary.size())

    dictionary.delete("age")
    dictionary.print_entries()
    print('Dictionary Size:', dictionary.size())
    print('Key "age":', dictionary.get("age"))
