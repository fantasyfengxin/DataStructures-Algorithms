"""A simple implementation of binary search tree."""

class Node:
	"""Tree node class."""
	def __init__(self, value, left_child, right_child):
		self.value = value
		self.left_child = left_child
		self.right_child = right_child


class BST:
	"""Simple binary search tree implementation."""
	def __init__(self):
		self.root = None

	def build_bst(self):
		"""build a bst from list of tree nodes"""
		pass

	def inorder_traverse(self):
		"""inorder traverse of the tree"""
		traversed_values = []
		self.inorder_traverse_helper(self.root, traversed_values)
		return traversed_values

	def inorder_traverse_helper(self, curr_node, traversed_values):
		"""a helper function to do real traverse."""
		if curr_node:
			traversed_values.append(curr_node.value)
			self.inorder_traverse_helper(curr_node.left_child, traversed_values)
			self.inorder_traverse_helper(curr_node.right_child, traversed_values)

	def inorder_traverse_gen(self, curr_node=self.root):
		"""inorder traverse generator."""
		if curr_node:
			yield curr_node.value
			if curr_node.left_child:
				yield from self.inorder_traverse_gen(curr_node.left_child)
			if curr_node.right_child:
				yield from self.inorder_traverse_gen(curr_node.right_child)

	def search(self, value):
		"""search value in the tree"""
		pass

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
		pass

	def insert(self, value):
		"""insert a node into the tree."""
		pass

	def delete(self, value):
		"""delete a node from the tree."""
		pass
