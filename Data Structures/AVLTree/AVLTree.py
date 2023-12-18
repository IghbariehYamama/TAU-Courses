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
	Time Complexity: O(log(n))
	
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):

		"""
		Recursive helper method for searching a node in the AVL tree.

		@type node: AVLNode
		@param node: the current node during the recursive search
		@type key: int
		@param key: the key to be searched
		@rtype: AVLNode
		@returns: the node corresponding to the key, or None if the key is not found
		"""
		def search_env(node, key):
			"""" Key is not found """
			if node.key is None:
				return
			"""" Key is found """
			if key == node.key:
				return node
			"""" Key is in the left subtree """
			if key < node.key:
				return search_env(node.left, key)
			"""" Key is in the right subtree """
			return search_env(node.right, key)

		return search_env(self.root, key)


	"""inserts val at position i in the dictionary
	Time Complexity: O(log(n))
	
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
		newNode.set_size(1)
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
			self.update_fields(y)
			y = y.parent

		return total_rotations


	"""
	Inserts a new node into the AVL tree following the rules of a binary search tree.
	Time Complexity: O(log(n))
	
	@type node: AVLNode
	@param node: the current node during the insertion process
	@type newNode: AVLNode
	@param newNode: the new node to be inserted
	"""
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


	"""
	Performs AVL rotations to rebalance the tree.
	Time Complexity: O(1)
	
	@type node: AVLNode
	@param node: the node at which rotations are performed
	@type bf: int
	@param bf: the balance factor of the node
	@rtype: int
	@returns: the number of rotations performed during AVL rebalancing
	"""
	def rotate(self, node, bf):
		"""" we check who is the criminal """
		if bf == -2:
			"""" what is the BF of the right son? """
			bf_right = node.right.left.height - node.right.right.height
			if bf_right == 1:
				self.right_rotate(node.right)
				self.left_rotate(node)
				return 2
			else:
				self.left_rotate(node)
				return 1
		else:
			"""" what is the BF of the left son? """
			bf_left = node.left.left.height - node.left.right.height
			if bf_left == -1:
				self.left_rotate(node.left)
				self.right_rotate(node)
				return 2
			else:
				self.right_rotate(node)
				return 1


	"""
	Performs a left rotation on the AVL tree.
	Time Complexity: O(1)
		
	@type node: AVLNode
	@param node: the node around which the rotation is performed
	"""
	def left_rotate(self, node):
		tmp = node.right.left
		node.right.left = node
		node.right.parent = node.parent
		"""" we check if the node was a left child or a right one to its parent """
		if node.parent is not None:
			if node.parent.right.key == node.key:
				node.parent.right = node.right
			else:
				node.parent.left = node.right
		else:
			self.root = node.right
		node.parent = node.right
		node.right = tmp
		tmp.parent = node
		"""" update the size and height fields """
		self.update_fields(node)


	"""
	Performs a right rotation on the AVL tree.
	Time Complexity: O(1)
	
	@type node: AVLNode
	@param node: the node around which the rotation is performed
	"""
	def right_rotate(self, node):
		tmp = node.left.right
		node.left.right = node
		node.left.parent = node.parent
		"""" we check if the node was a left child or a right one to its parent """
		if node.parent is not None:
			if node.parent.right.key == node.key:
				node.parent.right = node.left
			else:
				node.parent.left = node.left
		else:
			self.root = node.left
		node.parent = node.left
		node.left = tmp
		tmp.parent = node
		"""" update the size and height fields """
		self.update_fields(node)


	"""
	Updates the size and height fields of a given node.

	@type node: AVLNode
	@param node: the node for which size and height fields are updated
	"""
	def update_fields(self, node):
		node.set_size(node.left.get_size() + node.right.get_size() + 1)
		node.set_height(max(node.left.height, node.right.height) + 1)


	"""deletes node from the dictionary
	Time Complexity: O(log(n))
	
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		total_rotations = 0
		y = node.parent

		"""" First, we delete the node as we do in BST """
		self.BST_delete(node)

		"""" Then we go up and look for criminals while fixing the size and height of each node """
		while y != None:
			bf = y.left.height - y.right.height
			y.set_size(y.right.get_size() + y.left.get_size() + 1)
			if abs(bf) < 2:
				if y.height == max(y.left.height, y.right.height) + 1:
					y = y.parent
					break
				else:
					y.set_height(max(y.right.get_height(), y.left.get_height()) + 1)
					y = y.parent
			else:
				total_rotations += self.rotate(y, bf)
				y = y.parent

		"""" we continue to go up to update fields """
		while y != None:
			self.update_fields(y)
			y = y.parent

		return total_rotations


	def BST_delete(self, node):

		"""" Case 1: node is a leaf """
		if node.key is None and node.key is None:
			virtual_node = AVLNode(None, None)

			"""" The deleted node is the root """
			if node.parent is None:
				self.root = virtual_node
			else:
				if node.parent.right.key == node.key:

					"""" The deleted node is a right child """
					node.parent.right = virtual_node
				else:

					"""" The deleted node is a left child """
					node.parent.left = virtual_node

			"""" Case 2: node has two children """
		elif node.key is not None and node.key is not None:

			"""" Let y be the successor of node """
			y = self.successor(node)

			"""" Remove y from the tree """
			y.parent.left = y.right
			y.right.parent = y.parent

			"""" Replace node by y """
			y.parent = node.parent
			y.right = node.right
			y.left = node.left

			"""" The deleted node is the root """
			if node.parent is None:
				self.root = y
			else:
				if node.parent.right.key == node.key:

					"""" The deleted node is a right child """
					node.parent.right = y
				else:

					"""" The deleted node is a left child """
					node.parent.left = y
			node.right.parent = y
			node.left.parent = y
			node.left = None
			node.parent = None
			node.right = None

			"""" Case 3: node has only one child """
		else:
			if node.right.key is not None:
				child = node.right
				node.right = None
			else:
				child = node.left
				node.left = None

			"""" The deleted node is the root """
			if node.parent is None:
				self.root = child
				child.parent = None
			else:
				if node.parent.right.key == node.key:

					"""" The deleted node is a right child """
					node.parent.right = child
				else:

					"""" The deleted node is a left child """
					node.parent.left = child

			child.parent = node.parent
			node.parent = None


	def successor(self, node):
		y = node
		if y.right.key is None:

			"""" We go up until the first turn right """
			while y.parent is not None and y.parent.right.key == y.key:
				y = y.parent
			return y
		else:

			"""" Node has a right child, so we return the minimal node in the right subtree """
			y = node.right
			while y.key is not None:
				y = y.left

		return y.parent


	"""returns an array representing dictionary 
	Time Complexity: O(n)
	
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):

		"""
		Recursively traverses the AVL tree and populates an array with tuples (key, value).

		@type node: AVLNode
		@param node: the current node in the AVL tree
		@type array: list
		@param array: the list to store tuples (key, value)
		"""
		def avl_to_array(node, array):
			"""" The tree is done """
			if node is None or node.key is None:
				return
			"""" Go to the left subtree """
			avl_to_array(node.left, array)
			"""" Insert the current node """
			array.append((node.key, node.value))
			"""" Go to the right subtree """
			avl_to_array(node.right, array)
		array = []
		avl_to_array(self.root, array)
		return array


	"""returns the number of items in dictionary 
	Time Complexity: O(1)
	
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
	Time Complexity: O(log(n))
	
	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return None


	"""finds the i'th smallest item (according to keys) in self
	Time Complexity: O(log(n))
	
	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		return None


	"""returns the root of the tree representing the dictionary
	Time Complexity: O(1)
	
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root


	"""
	Prints a visual representation of the AVL tree, including virtual leaves.
	Credits: https://github.com/TotallyBot
	
	@type root: AVLNode
	@param root: the root of the AVL tree to be displayed
	"""
	def display(self, root):
		lines, *_ = self._display_aux(root)
		for line in lines:
			print(line)


	"""
	Internal helper method for displaying the AVL tree recursively.
	Credits: https://github.com/TotallyBot
	
	@type node: AVLNode
	@param node: the current node during the recursive display
	@rtype: tuple
	@returns: a tuple containing a list of strings representing each line of the display,
	          width, height, and horizontal coordinate of the root
	"""
	def _display_aux(self, node):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if not node.get_right() and not node.get_left():
			if not node.is_real_node():
				line = '%s' % "V"
			else:
				line = '%s' % node.get_key()

			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if not node.get_right() and node.get_left():
			lines, n, p, x = self._display_aux(node.get_left())
			s = '%s' % node.get_key()
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if not node.get_left() and node.get_right():
			lines, n, p, x = self._display_aux(node.get_right())
			s = '%s' % node.get_key()
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self._display_aux(node.get_left())
		right, m, q, y = self._display_aux(node.get_right())
		s = '%s' % node.get_key()
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2


tree1 = AVLTree()
tree1.insert(1,1)
tree1.insert(2,2)
tree1.insert(4,4)
tree1.insert(3,3)
tree1.display(tree1.root)
print(tree1.avl_to_array())
x = tree1.search(1)
i = tree1.search(2)
u = tree1.search(3)
k = tree1.search(4)
y = tree1.search(5)
