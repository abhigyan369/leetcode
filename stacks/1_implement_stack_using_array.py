# stack - can store any type of data
# mechanishm - lifo (last in first out)

'''
we have to these methods- push, pop, top, size
'''
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,x):
        self.items.append(x)
    def pop(self):
        if self.is_empty():
            return "cannot pop, stack is empty"
        return self.items.pop()
    def top(self):
        if self.is_empty():
            return "stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

st = Stack()
st.push(5)
st.push(7)
st.push(2)
print(st.size())
print(st)
st.pop()
st.pop()
st.top()
st.pop()
print(st)