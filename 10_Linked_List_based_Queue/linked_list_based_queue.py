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
        else:
            # Find the parent of the node to be deleted
            parent_node = self.get_parent_node(item_node)
            # If the node to be deleted is in between
            if self.tail == item_node:
                self.tail = parent_node
            if parent_node is not None:
                # Link the parent node to the next of the node to be deleted
                parent_node.next = item_node.next
        # Remove references to help with garbage collection
        item_node.next = None
        item_node.data = None
        # Decrease the length of the list by 1
        self.length -= 1

    # Delete the head node of the list Queue only allows deletion from head
    def delete_head(self):
        # If the list is empty, return None
        if self.head is None:
            return None
        else:
            # else, remove the head node and update the head to the next node (next node is the item below head)
            self.head = self.head.next
            # If the list becomes empty, update the tail to None
            if self.head is None:
                self.tail = None
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


class LinkedListQueue:
    def __init__(self):
        self.__list_queue = SinglyLinkedList()

    def en_queue(self, data):
        self.__list_queue.insert_last(data)

    def de_queue(self):
        if self.is_empty():
            return None
        head_data = self.__list_queue.head.data
        self.__list_queue.delete_head()
        return head_data

    def peek(self):
        if self.__list_queue.head is None:
            return None
        return self.__list_queue.head.data

    def is_empty(self):
        return self.__list_queue.length_of_list() == 0

    def size(self):
        return self.__list_queue.length_of_list()

    def print_queue(self):
        self.__list_queue.print_list()


if __name__ == "__main__":
    queue = LinkedListQueue()
    print("Is Queue empty?", queue.is_empty())
    queue.en_queue(10)
    queue.en_queue(20)
    queue.en_queue(30)
    print("Is Queue empty?", queue.is_empty())
    print("Size of Queue:", queue.size())
    queue.print_queue()
    print("Dequeue:", queue.de_queue())
    queue.print_queue()
    print("Peek:", queue.peek())
    print("Size of queue:", queue.size())  # 2
