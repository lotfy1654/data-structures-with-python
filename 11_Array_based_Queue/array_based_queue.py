# Array-based Queue Implementation
class ArrayBasedQueue:
    def __init__(self, capacity):
        # Create an array (list) of fixed size and set front, rear, and size
        self.__queue = [0] * capacity
        self.__capacity = capacity
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    def resize_one(self):
        print("Queue Overflow! Resizing the queue to additional one space.")
        # Increase capacity by one
        self.__capacity += 1
        # Create a new queue with the new capacity and copy elements
        new_queue = [0] * self.__capacity
        # Copy old elements to the new queue in correct order
        for i in range(self.__size):
            # Copy each element in circular manner
            new_queue[i] = self.__queue[(self.__front + i) % len(self.__queue)]
        # Point to the new queue
        self.__queue = new_queue
        # Reset front and rear pointers
        self.__front = 0
        # If size is greater than 0, rear should point to the last element
        self.__rear = self.__size - 1 if self.__size > 0 else -1

    # Enqueue an element to the rear of the queue
    def enqueue(self, data):
        # Check if the queue is full
        if self.is_full():
            self.resize_one()
        # Move rear to the next position in a circular manner
        self.__rear = (self.__rear + 1) % len(self.__queue)
        # Assign data to the rear position
        self.__queue[self.__rear] = data
        # Increment the size of the queue
        self.__size += 1

    # Dequeue an element from the front of the queue
    def de_queue(self):
        # Check if the queue is empty
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
        # Get the front element
        front_data = self.__queue[self.__front]
        # Optional: Clear the position (not necessary)
        self.__queue[self.__front] = None
        # Move front to the next position in a circular manner
        self.__front = (self.__front + 1) % len(self.__queue)
        # Decrement the size of the queue
        self.__size -= 1
        return front_data

    # Peek at the front element of the queue without removing it
    def peek(self):
        if self.is_empty():
            print("Queue Underflow! Cannot peek from an empty queue.")
            return None
        return self.__queue[self.__front]

    # Check if the queue is empty
    def is_empty(self):
        return self.__size == 0

    # Check if the queue is full
    def is_full(self):
        return self.__size == self.__capacity

    # Get the current size of the queue
    def size(self):
        return self.__size

    # Print the queue elements from front to rear
    def print_queue(self):
        print_data = ""
        if self.is_empty():
            print("Queue is empty.")
            return
        # Print elements in a circular manner from front to rear
        for i in range(self.__size):
            # Calculate the actual index in the circular queue
            index = (self.__front + i) % len(self.__queue)
            # Append the element to the print string
            print_data += str(self.__queue[index]) + " -> "
        print_data += "None"
        return print_data


if __name__ == "__main__":
    queue = ArrayBasedQueue(3)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.print_queue())
    queue.enqueue(50)  # This will trigger a resize
    print(queue.print_queue())
    print("Dequeued element:", queue.de_queue())
    print(queue.print_queue())
    print("Front element is:", queue.peek())
    print("Is queue full?", queue.is_full())
    print("Current queue size:", queue.size())
    queue.enqueue(40)
    queue.enqueue(50)  # This will trigger a resize
    print(queue.print_queue())
