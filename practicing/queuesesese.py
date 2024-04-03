#fifo basically a linked list 

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self, data):
        return self.queue[0]

    
