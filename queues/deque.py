'''
deque- double endend queue
it does not mean it is a queue, it is using doubly linked list
'''
from collections import deque

lst = deque([])

lst.append(1) # all operations are taking o(1) operations
lst.append(2)
lst.append(3)
lst.appendleft(69)
lst.popleft()
print(lst)