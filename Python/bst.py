
'''
Binary Search Tree

root.left.val  <  root. val
root.right.val >=  root.val
'''

from TreeNode import *

# Make sure that BST rules are held
# Returns bool
def valid(root):
	if not root:
		return
	elif (root.left and root.left.val > root.val) or (root.right and root.right.val < root.val):
		return False
	else:
		valid(root.left)
		valid(root.right)
		return True

# Takes a root TreeNode and inserts into the tree
def insert(root, val):
	if val < root.val and root.left == None:
		root.left = TreeNode(val)
	elif val >= root.val and root.right == None:
		root.right = TreeNode(val)
	elif val < root.val and root.left != None:
		return insert(root.left, val)
	elif val >= root.val and root.right != None:
		return insert(root.right, val)

def remove(root, val):
	# Found val to delete
	if root and (root.val == val or root.left.val == val or root.right.val == val):
		# Left node is val, and has no children
		if root.left.val == val and not root.left.left and not root.left.right:
			root.left = None
			return
		# Right node is val, and has no children
		elif root.right.val == val and not root.right.left and not root.right.right:
			root.right = None
			return
		# Left node is val, and has one child (left)
		elif root.left.val == val and root.left.left and not root.left.right:	
			root.left = root.left.left
			return
		# Left node is val, and has one child (right)
		elif root.left.val == val and root.left.right and not root.left.left:
			root.left = root.left.right
			return
		# Right node is val, and has one child (left)
		elif root.right.val == val and root.right.left and not root.right.right:
			root.right = root.right.left
			return
		# Right node is val, and has one child (right)
		elif root.right.val == val and root.right.right and not root.right.left:
			root.right = root.right.right
			return
		# Right node is val and has two children
		elif root.right.val == val:
			# Minimum val in right subtree
			small = smallest(root.right.right)
			# Repalce val of the node with found minimum
			root.right.val = small
			# Remove that duplicate
			remove(root.right, small)
		# Left node is val and has two children
		elif root.left.val == val:
			small = smallest(root.left.right)
			root.left.val = small
			remove(root.left, small)
		# root.val == val and has two children
		else:
			small = smallest(root.right)
			root.val = small
			remove(root.right, small)
	# Keep looking
	else:
		if not root:
			return
		if val < root.val:
			return remove(root.left, val)
		else:
			return remove(root.right, val)

# Returns the smallest number in the tree
def smallest(root):
	if not root.left and not root.right:
		return root.val
	# Smaller value to the left
	elif root.left:
		return smallest(root.left)
	# No val to left, but right val for sure to be bigger
	elif not root.left and root.right:
		return root.val

# Return the largest in the tree
# Helper function for remove
def largest(root):
	if not root.right and not root.left:
		ret = root.val
		return ret
	if root.right:
		return largest(root.right)
	

# Takes [list] of values and creates a tree
def make(list_of_values):
	if len(list_of_values) == 0:
		print 'No values given.'
	else:
		root = TreeNode(list_of_values[0])
		for i in xrange(1,len(list_of_values)):			#xrange over range
			insert(root,list_of_values[i])
		return root

# Looks for object and returns bool True if found
# Otherwise return bool False
def find(root, val):
	if root is None:
		return False
	elif val == root.val:
		return True
	elif val < root.val:
		return find(root.left, val)
	else:
		return find(root.right, val)

# Returns the leaves of the Tree
# Leaves are the outmost TreeNode that
# do not have a left or right TreeNode		
def leaves(root):
	if not root:
		return
	if not root.left and not root.right:
		print root.val
		return
	leaves(root.left)
	leaves(root.right)

# Will print all values of the tree starting from the
# small number to the highest number
def print_tree(root):
	if not root:
		return
	print_tree(root.left)
	print root.val
	print_tree(root.right)

# Uses tree_levels to print out the levels of the BST
def print_levels(root):
	i = 0
	l = []
	l = tree_levels(root, i, l)
	for i in xrange(0,len(l)):
		print 'Level ' + str(i)+ ': ' + str(l[i])

# Returns a list of lists with values in each level
# of the tree.
# D
def tree_levels(root, iterator, l):
	if not root:
		return
	if len(l) == iterator:
		l.append([root.val])
	else:
		l[iterator].append(root.val)
	iterator += 1
	tree_levels(root.left, iterator,l)
	tree_levels(root.right, iterator,l)
	return l