# Define the Singly Linked List Node
class LinkedListNode:
    # Initialize the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# Define The Linked List Iterator
class LinkedListIterator:
    def __init__(self, node):
        self.current_node = node

    def data(self):
        return self.current_node.data

    def next(self):
        self.current_node = self.current_node.next
        return self

    def current(self):
        return self.current_node

# Define the single linked list class
class SinglyLinkedList:
    # Initialize the linked list
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    # Add a node to the head of the list used in initialization
    def add_head(self, node):
        self.head = node
        self.tail = node

    # Insert a node at the end of the list
    def insert_last(self, data):
        # Create a new node with the given data
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, set head and tail to the new node
            self.head = new_node
            # Update the tail to the new node (the last node)
            self.tail = new_node
        else:
            # Append the new node at the end and update the tail (next of the current tail)
            self.tail.next = new_node
            # Update the tail to the new node (the last node)
            self.tail = new_node
        # Increment the length of the list
        self.length += 1

    # Insert a node after a given node
    def insert_after(self, prev_node, data):
        prev_node = self.get_node(prev_node)
        if prev_node is None:
            return
        new_node = LinkedListNode(data)
        # Link the new node to the next of the previous node
        new_node.next = prev_node.next
        # Link the previous node to the new node
        prev_node.next = new_node
        # If the new node is inserted at the end, update the tail
        if new_node.next is None:
            self.tail = new_node
        self.length += 1

    # Insert a node before a given node
    def insert_before(self, next_node, data):
        next_node = self.get_node(next_node)
        if next_node is None:
            return
        # Create a new node with the given data
        new_node = LinkedListNode(data)
        # Link the new node to the next node
        new_node.next = next_node
        # Find the parent of the next node
        parent_node = self.get_parent_node(next_node)
        # If the next node is the head node
        if parent_node is None:
            self.head = new_node
        else:
            # Link the parent node to the new node
            parent_node.next = new_node
        self.length += 1

    # Delete a given node from the list
    def delete_node(self, node):
        # Find the node to be deleted
        item_node = self.get_node(node)
        # Find the parent of the node to be deleted
        parent_node = self.get_parent_node(item_node)
        # If the node is not found, return
        if item_node is None:
            return
        # If the list has only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the node to be deleted is the head node
        elif self.head == item_node:
            self.head = item_node.next
        # If the node to be deleted is the tail node
        elif parent_node is None:
            self.head = item_node.next
        else:
            # If the node to be deleted is in between
            if self.tail == item_node:
                self.tail = parent_node
            else:
                # Bypass the node to be deleted
                parent_node.next = item_node.next
        self.length -= 1

    # Get node for specified data
    def get_node(self, data):
        # Start from the head of the list
        itr = self.begin()
        # Traverse the list until the end
        while itr.current() is not None:
            # .data() returns the data of the current node comes from iterator
            if itr.data() == data:
                return itr.current()
            itr.next()
        return None

    # Get the parent node of a given child node
    def get_parent_node(self, child_node):
        # Start from the head of the list
        itr = self.begin()
        # Traverse the list until the end
        while itr.current() is not None:
            if itr.current().next == child_node:
                return itr.current()
            itr.next()
        return None

    # Get the length of the list
    def length_of_list(self):
        return self.length

    # Print the linked list
    def print_list(self):
        # Start from the head of the list
        itr = self.begin()
        # Traverse the list until the end
        while itr.current() is not None:
            print(itr.data(), "->", end=" ")
            itr.next()
        print("END")

    # Return an iterator to the beginning of the list to access nodes [ head  -> next -> next -> ... -> tail ]
    def begin(self):
        itr = LinkedListIterator(self.head)
        return itr


if __name__ == "__main__":
    list = SinglyLinkedList()
    list.insert_last(10)
    list.insert_last(20)
    list.insert_last(30)
    list.print_list()
    print("Length of the list:", list.length_of_list())
    list.insert_after(20, 25)
    list.print_list()
    list.insert_before(25, 22)
    list.print_list()

    list.delete_node(10)
    list.print_list()
    print(list.head.data)
