
'''
Binary Search Tree

root.left.val  <  root. val
root.right.val >=  root.val
'''

from TreeNode import *

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

# Look through the tree to find the value to remove
# Once we find the value, replace it with the largest
# value in the left subtree
def remove(root, val):
	if not root:
		print 'Value not in BST'
		return
	elif val == root.val:		# Now we replace it
		root.val = largest(root.left)
	elif val < root.val:
		return remove(root.left, val)
	else:
		return remove(root.right, val)

# Return the largest in the tree
# Helper function for remove
def largest(root):
	if not root.right and not root.left:
		ret = root.val
		del(root)
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