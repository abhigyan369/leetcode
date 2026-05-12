'''
queue- mechnism - fifo first in first out

'''
class Queue:
    def __init__(self):
        self.items = []
    def front(self):
        if len(self.items) == 0:
            return "there is no element in queue"
        return self.items[0]
    def enqueue(self, x):
        return self.items.append(x)
    def dequeue(self):
        if len(self.items) == 0:
            return "cannot pop, no element in the stack"
        return self.items.remove(self.items[0])
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
print(q.front())