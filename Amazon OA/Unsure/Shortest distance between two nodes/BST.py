# Python3 program to find distance between
# two nodes in BST
class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None

# Standard BST insert function
def insert(root, key):
	if root == None:
		root = newNode(key)
	elif root.key > key:
		root.left = insert(root.left, key)
	elif root.key < key:
		root.right = insert(root.right, key)
	return root

# This function returns distance of x from
# root. This function assumes that x exists
# in BST and BST is not NULL.
def distanceFromRoot(root, x):
	if root.key == x:
		return 0
	elif root.key > x:
		return 1 + distanceFromRoot(root.left, x)
	return 1 + distanceFromRoot(root.right, x)

# Returns minimum distance beween a and b.
# This function assumes that a and b exist
# in BST.
def distanceBetween2(root, a, b):
	if root == None:
		return 0

	# Both keys lie in left
	if root.key > a and root.key > b:
		return distanceBetween2(root.left, a, b)

	# Both keys lie in right
	if root.key < a and root.key < b: # same path
		return distanceBetween2(root.right, a, b)

	# Lie in opposite directions
	# (Root is LCA of two nodes)
	if root.key >= a and root.key <= b:
		return (distanceFromRoot(root, a) +
				distanceFromRoot(root, b))

# This function make sure that a is smaller
# than b before making a call to findDistWrapper()
def findDistWrapper(root, a, b):
	if a > b:
		a, b = b, a
	return distanceBetween2(root, a, b)

# Driver code
if __name__ == '__main__':
	root = None
	root = insert(root, 20)
	insert(root, 10)
	insert(root, 5)
	insert(root, 15)
	insert(root, 30)
	insert(root, 25)
	insert(root, 35)
	a, b = 5, 55
	print(findDistWrapper(root, 5, 35))

# This code is contributed by PranchalK
