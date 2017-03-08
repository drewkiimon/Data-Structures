'''
Let's make a linked list!

Rule of thumb (note for myself)
- We have a head, then a iterative head
- Head points to head of linked list
- Iterative head is the one we can go through
- Think of pointers
'''
from Node import *

# Finds the val and returns True if in the list
# Returns false otherwise
def find(head, val):
	while head:
		if head.val == val:
			return True
		else:
			head = head.next
	return False

# Inserting value into linked list
# Insertion happens at the tail
def tail_insert(head, val):
	ret = head
	while head:
		if head.next == None:
			head.next = Node(val)
			return ret
		head = head.next

# Inserting value into linked list
# Insertion happens at the head
def head_insert(head, val):
	ret = Node(val)
	ret.next = head
	return ret

# Find value and remove it from Linked List
def remove(head, val):
	ret = head
	while head:
		if head.val == val:
			head = head.next
			ret = head
			return ret
		if head.next.val == val:
			head.next = head.next.next
			return ret
		else:
			head = head.next
	return ret

# Reverse linked list
def reverse(head):
	prev = None
	cur = head
	while cur:
		next = cur.next		# Gets "rid" of head of head
		cur.next = prev		# Current val's next is prev
		prev = cur
		cur = next			# We have a new current
	return prev

# Reversing specific section of linked list
# Head, start value, end value
def s_reverse(head, start, end):
	print "special reverse"

# Returns a created Linked List from a list of values
def make(l):
	head = Node(l[0])				# This head is for iterating through
	ret_head = head					#This is pointing to the HEAD of taile
	for value in xrange(1,len(l)):
		head.next = Node(l[value])
		head = head.next
	return ret_head
	
# Prints a visual of the list
def print_list(head):
	ret = []
	while head:
		ret.append(str(head.val))
		head = head.next
	ret.append("None")
	print '->'.join(ret)