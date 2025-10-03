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

    # Define Insert First for Stack
    def insert_first(self, data):
        new_node = LinkedListNode(data)
        # If the list is empty, set head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Else, insert the new node at the beginning
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Define Delete Head for Stack
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

# Define the Stack class using Singly Linked List


class Stack:
    # Initialize the stack
    def __init__(self):
        # Create an instance of SinglyLinkedList to store stack elements
        # List is private to prevent direct access from outside the class
        self.__list = SinglyLinkedList()

    # Push an item onto the stack
    def push(self, data):
        self.__list.insert_first(data)

    # Pop an item off the stack
    def pop(self):
        # If the stack is empty, return None
        if self.__list.length_of_list() == 0:
            return None
        # Get the data of the head node (top of the stack)
        top_data = self.__list.head.data
        # Delete the head node (pop the top of the stack)
        self.__list.delete_head()
        # Return the data of the popped node
        return top_data

    # Peek at the top item of the stack without removing it
    def peek(self):
        if self.__list.length_of_list() == 0:
            return None
        # Get the data of the head node (top of the stack)
        head_data = self.__list.head.data
        return head_data

    # Check if the stack is empty
    def is_empty(self):
        return self.__list.length_of_list() == 0

    # Get the size of the stack
    def size(self):
        return self.__list.length_of_list()

    # Print the stack elements
    def print_stack(self):
        self.__list.print_list()


if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack size:", stack.size())  # 3
    print("Top element:", stack.peek())  # 30
    print("Popped element:", stack.pop())  # 30
    print("Stack size after pop:", stack.size())  # 2
    print("Is stack empty?", stack.is_empty())  # False
    stack.print_stack()  # 20 -> 10 -> END
    print("Top element:", stack.peek())  # 20
