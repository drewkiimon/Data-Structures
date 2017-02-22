'''
A test script for using my Binary Search Tree functions
and making sure that they do what they should be doing.

Code written by Andrew Pagan
'''

from TreeNode import *
from bst import *

l = [5,3,4,6,10,5,1,2]
print l

print 'root made'
root = make(l)

print 'print_tree'
print_tree(root)

print 'leaves'
leaves(root)

print 'looking for 11'
print find(root,11)

print 'insert 11'
insert(root,11)

print 'looking for 11'
print find(root,11)

print 'print_levels'
print_levels(root)

print 'removing 1'
remove(root, 1)				#Still needs to be fixed. Ugh

print 'reprint of levels'
print_levels(root)

print 'valid?'
print valid(root)

test = TreeNode(5)
test.right = TreeNode(3)
print valid(test)
print test.val, test.right.val
print 'end of test'