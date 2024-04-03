CAPACITY = 10

# maximum heap
class Heap:
    
    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*CAPACITY

    def insert(self, item):
        
        if self.heap_size == CAPACITY:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        self.fix_up(self.heap_size - 1)

    # validating the structure starting with current node 
    # up to the root node
    # O(logN)
    def fix_up(self, index):
        parent_index = (index - 1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max_item = self.get_max()
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size = self.heap_size - 1

        # heapify
        self.fix_down(0)

        return max_item

    # opposite of fix_up in terms of vector of progression
    # O(logN)
    def fix_down(self, index):

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        largest_index = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # checks if largest_index was changed by previous conditionals
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):
        # logn for the poll function
        # n * logn = O(NlogN)
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


heap = Heap()
heap.insert(13)
heap.insert(-2)
heap.insert(0)
heap.insert(8)
heap.insert(1)
heap.insert(-5)
heap.insert(99)
heap.insert(133)
heap.insert(200)
heap.insert(-50)


heap.heap_sort()