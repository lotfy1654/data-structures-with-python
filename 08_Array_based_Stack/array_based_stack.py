# Array-based Stack Implementation
class ArrayBasedStack:
    # Initialize the stack with a fixed capacity
    def __init__(self, capacity):
        # Create an array (list) of fixed size and set top to -1
        self.__stack = [0] * capacity
        self.__capacity = capacity
        self.__top = -1

    # Resize the stack by increasing its capacity by one
    def resize_one(self):
        print("Stack Overflow! Resizing the stack to additional one space.")
        # Increase capacity by one
        self.__capacity += 1
        # Create a new stack with the new capacity and copy elements
        new_stack = [0] * self.__capacity
        # Copy old elements to the new stack
        for i in range(self.__top + 1):
            # Copy each element
            new_stack[i] = self.__stack[i]
        # Point to the new stack
        self.__stack = new_stack

    # Push an element onto the stack
    def push(self, data):
        # Check if the stack is full
        if self.is_full():
            self.resize_one()
        self.__top += 1            # increment the top
        self.__stack[self.__top] = data  # assign data

    # Pop an element from the stack
    def pop(self):
        # Check if the stack is empty
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        # Remove the top element and return it without losing it
        head_data = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        return head_data

    # Peek at the top element of the stack without removing it
    def peek(self):
        if self.is_empty():
            print("Stack Underflow! Cannot peek from an empty stack.")
            return None
        return self.__stack[self.__top]

    # Check if the stack is empty
    def is_empty(self):
        return self.__top == -1

    # Check if the stack is full
    def is_full(self):
        return self.__top == self.__capacity - 1

    # Get the current size of the stack
    def size(self):
        return self.__top + 1

    # Print the stack elements from top to bottom
    def print_stack(self):
        print_data = ""
        if self.is_empty():
            print("Stack is empty.")
            return
        for i in range(self.__top, -1, -1):
            print_data += str(self.__stack[i]) + " -> "
        return print_data.strip()


if __name__ == "__main__":
    stack = ArrayBasedStack(3)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.print_stack())
    print(stack.print_stack())
    print("Popped element:", stack.pop())
    print(stack.print_stack())
    print("Top element:", stack.peek())
    print("Is stack empty?", stack.is_empty())
    print("Is stack full?", stack.is_full())
    print("Current stack size:", stack.size())
    stack.push(40)
    stack.push(50)  # This will trigger a resize
    print(stack.print_stack())
