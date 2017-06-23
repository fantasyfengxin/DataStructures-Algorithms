"""A simple implementation of binary search tree."""

class Node:
	"""Tree node class."""
	def __init__(self, value, left_child=None, right_child=None):
		self.value = value
		self.left_child = left_child
		self.right_child = right_child


class BST:
	"""Simple binary search tree implementation."""
	def __init__(self):
		self.root = None

	def inorder_traverse(self):
		"""inorder traverse of the tree"""
		traversed_values = []
		self.inorder_traverse_helper(self.root, traversed_values)
		return traversed_values

	def inorder_traverse_helper(self, curr_node, traversed_values):
		"""a helper function to do real traverse."""
		if curr_node:
			self.inorder_traverse_helper(curr_node.left_child, traversed_values)
			traversed_values.append(curr_node.value)
			self.inorder_traverse_helper(curr_node.right_child, traversed_values)

	def inorder_traverse_gen(self, curr_node='start'):
		"""inorder traverse generator."""
		if curr_node == 'start':
			curr_node = self.root
		if curr_node:
			if curr_node.left_child:
				yield from self.inorder_traverse_gen(curr_node.left_child)

			yield curr_node.value

			if curr_node.right_child:
				yield from self.inorder_traverse_gen(curr_node.right_child)

	def search(self, value):
		"""search value in the tree"""
		curr_node = self.root
		while True:
			if not curr_node:
				return False
			elif value < curr_node.value:
				curr_node = curr_node.left_child
			elif value > curr_node.value:
				curr_node = curr_node.right_child
			else:
				return True
		return False

	def maximum(self):
		"""return maximum value of the tree"""
		if self.root:
			curr_node = self.root
			while curr_node:
				curr_node = curr_node.right_child
			return curr_node.value

	def minimum(self):
		"""return minimum value of the tree."""
		if self.root:
			curr_node = self.root
			while curr_node:
				curr_node = curr_node.left_child
			return curr_node.value

	def successor(self, node):
		"""return the successor of node in the tree."""
		if node.right_child:
			curr_node = node.right_child
			while curr_node.left_child:
				curr_node = curr_node.left_child
			return curr_node
		traversed = [(self.root, None)]
		curr_node = self.root
		while curr_node:
			if node.value == curr_node.value:
				break
			elif node.value <= curr_node.value:
				curr_node = curr_node.left_child
				traversed.append((curr_node, 'left'))
			else:
				curr_node = curr_node.right_child
				traversed.append((curr_node, 'right'))
		if not curr_node:
			print('Input node is not in the tree...')
			return
		ancestor = traversed.pop()
		while ancestor[1] and ancestor[1] == 'right':
			ancestor = traversed.pop()
		if not ancestor[1]:
			print('Input node is the largest node in the tree....')
		else:
			return traversed.pop()[0]

	def insert(self, value):
		"""insert a node into the tree."""
		to_insert = Node(value)
		if not self.root:
			self.root = to_insert
		else:
			curr_node = self.root
			while True:
				if value <= curr_node.value:
					if curr_node.left_child:
						curr_node = curr_node.left_child
						continue
					else:
						curr_node.left_child = to_insert
						break
				if value >= curr_node.value:
					if curr_node.right_child:
						curr_node = curr_node.right_child
						continue
					else:
						curr_node.right_child = to_insert
						break

	def delete(self, value):
		"""delete a node from the tree."""
		if not self.search(value):
			print('to delete node does not exists...')
			return
		parrent_node, curr_node = None, self.root
		while True:
			if value == curr_node.value:
				break
			elif value <= curr_node.value:
				parrent_node = curr_node
				curr_node = curr_node.left_child
			else:
				parrent_node = curr_node
				curr_node = curr_node.right_child
		# if to delete node is a leaf node
		if (not curr_node.left_child) and (not curr_node.right_child):
			if parrent_node.left_child == curr_node:
				parrent_node.left_child = None
			else:
				parrent_node.right_child = None
		elif not curr_node.left_child:
			if parrent_node.left_child == curr_node:
				parrent_node.left_child = curr_node.right_child
			else:
				parrent_node.right_child = curr_node.right_child
		elif not curr_node.right_child:
			if parrent_node.left_child == curr_node:
				parrent_node.left_child = curr_node.left_child
			else:
				parrent_node.right_child = curr_node.left_child
		elif not parrent_node:  # to delete the root node
			left_child = curr_node.left_child
			right_most = left_child
			while right_most.right_child:
				right_most = right_most.right_child
			right_most.right_child = curr_node.right_child
			curr_node.left_child = None
			curr_node.right_child = None
			self.root = left_child
		else:
			left_child = curr_node.left_child
			right_most = left_child
			while right_most.right_child:
				right_most = right_most.right_child
			right_most.right_child = curr_node.right_child
			curr_node.left_child = None
			curr_node.right_child = None
			if parrent_node.left_child == curr_node:
				parrent_node.left_child = left_child
			else:
				parrent_node.right_child = left_child

