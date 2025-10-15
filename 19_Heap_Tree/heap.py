# Heap implementation in Python

import math


class Heap:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    # Min-Heap insert operation
    def insert_new_data(self, data):
        # Insert at the end and bubble up
        i = self.size
        # Insert the new element
        self.heap_list.insert(i, data)
        # Increase size
        self.size += 1
        # Get parent index
        parent_index = (i - 1) // 2
        # Percolate up or bubble up
        while i != 0 and self.heap_list[i] < self.heap_list[parent_index]:
            self.heap_list[parent_index], self.heap_list[i] = self.heap_list[i], self.heap_list[parent_index]
            i = parent_index
            parent_index = (i - 1) // 2

        return self.heap_list

    # Remove The Minimum Element (Root) & Move Last Element To Root & Percolate Down To Restore Heap Property
    def delete_min(self):  # Min-Heap
        if self.size == 0:
            return None

        i = 0
        # store root to return later
        old_root = self.heap_list[0]
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
            if left_index < self.size and self.heap_list[left_index] < self.heap_list[smallest_index]:
                smallest_index = left_index

            # Check if right child exists and is smaller than left child
            if right_index < self.size and self.heap_list[right_index] < self.heap_list[left_index]:
                smallest_index = right_index

            # Check if right child exists and is smaller than current smallest
            if self.heap_list[smallest_index] >= self.heap_list[i]:
                break

            # Swap and continue percolating down
            self.heap_list[smallest_index], self.heap_list[i] = self.heap_list[i], self.heap_list[smallest_index]
            i = smallest_index
            left_index = (2 * i) + 1

        return old_root

    # Get the size of the heap
    def size(self):
        return self.size

    def print_heap(self):
        print("Heap Array Representation:", self.heap_list)
        for i in range(self.size):
            print(f" {self.heap_list[i]}", end=" -> ")
        print("\n")

    def draw(self):
        if self.size == 0:
            print("Heap is empty")
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
                line += str(self.heap_list[j]) + " " * space_between
                j += 1

            print("\n" + line)


if __name__ == "__main__":
    heap = Heap()
    heap.insert_new_data(10)
    heap.insert_new_data(20)
    heap.insert_new_data(5)
    heap.insert_new_data(6)
    heap.insert_new_data(1)
    heap.insert_new_data(8)
    heap.print_heap()
    # heap.draw()

    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    print("Root element removed:", heap.delete_min())
    heap.print_heap()
    heap.draw()

    heap.insert_new_data(10)
    heap.insert_new_data(20)
    heap.insert_new_data(5)
    heap.insert_new_data(6)
    heap.insert_new_data(1)
    heap.insert_new_data(8)
    heap.print_heap()
    heap.draw()
