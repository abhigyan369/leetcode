'''
queue- mechnism - fifo first in first out

'''
class Queue:
    def __init__(self):
        self.items = []
    def top(self):
        if len(self.items) == 0:
            return "there is no element in queue"
        return self.items[0]
    def push(self, x):
        return self.items.append(x)
    def pop(self):
        if len(self.items) == 0:
            return "cannot pop, no element in the stack"
        return self.items.remove(self.items[0])
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q)
q.pop()
print(q)