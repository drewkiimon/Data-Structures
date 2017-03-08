# Test for queue

from queue import *

x = Queue()
print x.empty()
x.push(3)
x.push(10)
x.push(4)
x.push(7)
x.push(-2)
x.view()
print x.size()
print x.front()
print x.back()
print x.pop()
print x.pop()
x.view()