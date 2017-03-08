'''
Testing linked list functions
'''

from Node import *
from linkedlist import *

print '________________'
l = [6,3,4,1,2]
print l
head = make(l)
print '________________'
print_list(head)
print '________________'
print 'Deleting 4'
head = remove(head,4)
print_list(head)
print 'Deleting 6'
head = remove(head,6)
print_list(head)
print '________________'
print 'Insert 4 into tail'
head = tail_insert(head,4)
print_list(head)
print 'Insert 7 into head'
head = head_insert(head,7)
print_list(head)
print '________________'
print 'Reverse'
head = reverse(head)
print_list(head)
print '________________'
print 'Find'
print find(head,6)
print  find(head,3)
print '________________'
print 'Print list backwards'