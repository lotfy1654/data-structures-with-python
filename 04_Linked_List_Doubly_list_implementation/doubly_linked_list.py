# Define the Doubly Linked List Node
class LinkedListNode:
    # Initialize the node with data , next pointer and back pointer
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

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

# Define the doubly linked list class


class DoublyLinkedList:
    # Initialize the linked list
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    # # Add a node to the head of the list used in initialization
    # def add_head(self, node):
    #     self.head = node
    #     self.tail = node

    # Insert a node after a given node
    def insert_after(self, prev_data, data):
        # Get the previous node using the data
        prev_node = self.get_node(prev_data)
        # Make node from the new data
        new_node = LinkedListNode(data)
        # Make new_node point to the next of previous node
        new_node.next = prev_node.next
        # Make new_node back point to the previous node
        new_node.back = prev_node
        # Make previous node point to the new_node
        prev_node.next = new_node
        # If new_node is the last node, update the tail pointer
        if new_node.next is None:
            self.tail = new_node
        # Else make the next node's back point to the new_node
        else:
            new_node.next.back = new_node
        # Increase the length of the list
        self.length += 1

    # Insert a node at the end of the list
    def insert_last(self, data):
        # Make node from the new data
        new_node = LinkedListNode(data)
        # If the list is empty, make the new node the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Else, make the new node the next of the tail and update the tail pointer
        else:
            self.tail.next = new_node
            new_node.back = self.tail
            self.tail = new_node
        # Increase the length of the list
        self.length += 1

    # Insert a node before a given node
    def insert_before(self, next_data, new_data):
        # Get the next node using the data
        next_node = self.get_node(next_data)
        # Make node from the new data
        new_node = LinkedListNode(new_data)
        # Make new_node point to the next node
        new_node.next = next_node
        # If the next node is the head, update the head pointer
        if next_node.back is None:
            # Make the new node the head and update the back pointer of the next node
            self.head = new_node
            next_node.back = new_node
            new_node.back = None
        # Else, make the new_node back point to the previous node and update the pointers
        else:
            new_node.back = next_node.back
            next_node.back.next = new_node
            next_node.back = new_node
        self.length += 1

    # Delete a given node from the list
    def delete_node(self, data_to_delete):
        # Get the node to delete using the data
        node_to_delete = self.get_node(data_to_delete)
        # If the node to delete is the head, update the head pointer
        if node_to_delete == self.head and node_to_delete.back is None:
            node_to_delete.next.back = None
            self.head = node_to_delete.next
        # If the node to delete is the tail, update the tail pointer
        elif node_to_delete == self.tail and node_to_delete.next is None:
            node_to_delete.back.next = None
            self.tail = node_to_delete.back
        # If the node to delete is head and tail, make the head and tail None
        elif node_to_delete == self.head and node_to_delete == self.tail:
            self.head = None
            self.tail = None
        # Else node to delete is in the middle of the list
        else:
            # Make the next node's back point to the previous node
            node_to_delete.next.back = node_to_delete.back
            # Make the previous node's next point to the next node
            node_to_delete.back.next = node_to_delete.next
        # Remove references to help with garbage collection
        node_to_delete.next = None
        node_to_delete.back = None
        node_to_delete.data = None
        # Decrease the length of the list
        self.length -= 1

    # Create a copy of the list
    def copy(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.insert_last(current.data)  # Copy data into new nodes
            current = current.next
        return new_list

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
    list = DoublyLinkedList()
    list.insert_last(10)
    list.insert_last(20)
    list.insert_last(30)
    list.print_list()
    print("Length of the list:", list.length_of_list())
    list.insert_after(20, 25)
    list.print_list()
    list.insert_before(25, 22)
    list.print_list()
    list.delete_node(20)
    list.print_list()
    list_copy = list.copy()
    list_copy.insert_last(40)
    list_copy.print_list()
    print(list.head.data)
