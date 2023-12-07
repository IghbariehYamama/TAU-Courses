#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key is None


"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here



	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):
		return None


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		total_rotations = 0
		"""" first we add the node as we do in BST """
		newNode = AVLNode(key, val)
		if self.root is None:
			self.root = newNode
		else:
			self.BST_insert(self.root, newNode)
		newNode.set_height(0)
		newNode.set_size(0)
		newNode.right = AVLNode(None, None)
		newNode.left = AVLNode(None, None)

		"""" then we go up and look for criminals while fixing the size and height of each node """
		y = newNode.parent
		while y != None:
			bf = y.left.height - y.right.height
			y.set_size(y.right.get_size() + y.left.get_size() + 1)
			if abs(bf) < 2:
				if y.height == max(y.left.height, y.right.height)+1:
					y = y.parent
					break
				else:
					y.set_height(max(y.right.get_height(), y.left.get_height()) + 1)
					y = y.parent
			else:
				total_rotations = self.rotate(y, bf)
				y = y.parent
				break

		"""" we continue to go up to update fields """
		while y != None:
			update_fields(y)
			y = y.parent

		return total_rotations


	def rotate(self, node, bf):
		"""" we check who is the criminal """
		if bf == -2:
			"""" what is the BF of the right son? """
			bf_right = node.right.left.height - node.right.right.height
			if bf_right == -1:
				left_rotate(node)
				return 1
			else:
				right_rotate(node.right)
				left_rotate(node)
				return 2
		else:
			"""" what is the BF of the left son? """
			bf_left = node.left.left.height - node.left.right.height
			if bf_left == -1:
				left_rotate(node.left)
				right_rotate(node)
				return 2
			else:
				right_rotate(node)
				return 1


	def left_rotate(self, node):
		tmp = node.right.left
		node.right.left = node
		node.right.parent = node.parent
		"""" we check if the node was a left child or a right one to its parent """
		if node.parent.right.key == node.key:
			node.parent.right = node.right
		else:
			node.parent.left = node.right
		node.parent = node.right
		node.right = tmp
		tmp.parent = node
		"""" update the size and height fields """
		update_fields(node)


	def right_rotate(self, node):
		tmp = node.left.right
		node.left.right = node
		node.left.parent = node.parent
		"""" we check if the node was a left child or a right one to its parent """
		if node.parent.right.key == node.key:
			node.parent.right = node.left
		else:
			node.parent.left = node.left
		node.parent = node.left
		node.left = tmp
		tmp.parent = node
		"""" update the size and height fields """
		update_fields(node)


	"""" update the size and height fields """
	def update_fields(self, node):
		node.set_size(node.left.get_size() + node.right.get_size() + 1)
		node.set_height(max(node.left.height, node.right.height) + 1)


	def BST_insert(self, node, newNode):
		if newNode.key < node.key:
			if node.left.key is None:
				node.left = newNode
				newNode.parent = node
			else:
				self.BST_insert(node.left, newNode)
		else:
			if node.right.key is None:
				node.right = newNode
				newNode.parent = node
			else:
				self.BST_insert(node.right, newNode)


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	
	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined +1
	"""
	def join(self, tree, key, val):
		return None


	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return None


	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root


tree1 = AVLTree()
tree1.insert(3,3)
print(tree1)
tree1.insert(1,1)
print(tree1)
tree1.insert(4,4)
print(tree1)
tree1.insert(2,2)
print(tree1)

