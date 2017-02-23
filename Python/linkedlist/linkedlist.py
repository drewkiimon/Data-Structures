'''
Let's make a linked list!

Rule of thumb (note for myself)
- We have a head, then a iterative head
- Head points to head of linked list
- Iterative head is the one we can go through
- Think of pointers
'''
from Node import *

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
	if not head:
		return
	reverse(head.next)
	print head.val

# Returns a created Linked List from a list of values
def make(l):
	head = Node(l[0])				# This head is for iterating through
	ret_head = head					#This is pointing to the HEAD of taile
	for value in xrange(1,len(l)):
		head.next = Node(l[value])
		head = head.next
		print head.val
	return ret_head
	

def print_list(head):
	while head:
		print head.val
		head = head.next