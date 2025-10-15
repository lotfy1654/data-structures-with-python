# Priority Queue implementation using a Min-Heap

import math

# Class to represent an item in the priority queue with its priority and data


class PriorityQueueItem:
    def __init__(self,  priority, data):
        self.priority = priority
        self.data = data


class PriorityQueue:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    # Min-Heap insert operation
    def enqueue(self, priority, data):
        item = PriorityQueueItem(priority, data)
        # Insert at the end and bubble up
        i = self.size
        # Insert the new element
        self.heap_list.insert(i, item)
        # Increase size
        self.size += 1
        # Get parent index
        parent_index = (i - 1) // 2
        # Percolate up or bubble up
        while i != 0 and self.heap_list[i].priority < self.heap_list[parent_index].priority:
            self.heap_list[parent_index], self.heap_list[i] = self.heap_list[i], self.heap_list[parent_index]
            i = parent_index
            parent_index = (i - 1) // 2

        return self.heap_list

    # Remove The Minimum Element (Root) & Move Last Element To Root & Percolate Down To Restore Heap Property
    def dequeue(self):  # Min-Heap
        if self.size == 0:
            return None

        i = 0
        # store root to return later
        old_root = self.heap_list[0].data
        old_root_priority = self.heap_list[0].priority
        self.heap_list[i] = self.heap_list[self.size - 1]
        # Use pop() to remove last element from the list and decrease size
        self.heap_list.pop()
        self.size -= 1
        # Get left child index
        left_index = (2 * i) + 1
        while (left_index < self.size):
            # Get right child index
            right_index = (2 * i) + 2
            # Assume left child is the smallest for now
            smallest_index = i

            # Check if left child exists and is smaller than current smallest
            if left_index < self.size and self.heap_list[left_index].priority < self.heap_list[smallest_index].priority:
                smallest_index = left_index

            # Check if right child exists and is smaller than left child
            if right_index < self.size and self.heap_list[right_index].priority < self.heap_list[left_index].priority:
                smallest_index = right_index

            # Check if right child exists and is smaller than current smallest
            if self.heap_list[smallest_index].priority >= self.heap_list[i].priority:
                break

            # Swap and continue percolating down
            self.heap_list[smallest_index], self.heap_list[i] = self.heap_list[i], self.heap_list[smallest_index]
            i = smallest_index
            left_index = (2 * i) + 1

        return PriorityQueueItem(old_root, old_root_priority)

    # Check if the heap is empty
    def isEmpty(self):
        return self.size == 0

    # Get the size of the heap
    def size(self):
        return self.size

    def print_priority_queue(self):
        for i in range(self.size):
            print(
                f"Data: {self.heap_list[i].data}, Priority: {self.heap_list[i].priority}", end=" | ")
        print("\n")

    def draw(self):
        if self.size == 0:
            print("Priority Queue is empty")
            return

        levels_count = math.floor(math.log2(self.size)) + 1
        line_width = 2 ** (levels_count - 1)

        j = 0
        for i in range(levels_count):
            nodes_count = 2 ** i
            space = int(line_width - nodes_count / 2)
            space_between = max(1, levels_count // nodes_count)
            k = j
            line = " " * (space + space_between)

            for _ in range(nodes_count):
                if j == self.size:
                    break
                line += str(self.heap_list[j].data) + " " * space_between
                j += 1

            print("\n" + line)


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    priority_queue.enqueue(5, "Task 5")
    priority_queue.enqueue(1, "Task 1")
    priority_queue.enqueue(3, "Task 3")
    priority_queue.enqueue(4, "Task 4")
    priority_queue.enqueue(2, "Task 2")
    priority_queue.print_priority_queue()
    priority_queue.draw()

    while not priority_queue.isEmpty():
        item = priority_queue.dequeue()
        print(
            f"Dequeued item with priority {item.priority} and data '{item.data}'")
        priority_queue.print_priority_queue()
