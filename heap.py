"""A simple max heap implementation for practice.
"""

class MaxHeap:
	def __init__(self, elements):
		self.elements = elements
		self.heap_size = len(self.elements)
		self.build_heap()

	def build_heap(self):
		last_index = self.heap_size - 1
		last_non_leaf = self._parent(last_index)
		print(last_non_leaf)
		for index in range(last_non_leaf, -1, -1):
			self.max_heapify(index)

	def max_heapify(self, index):
		"""Keep the tree rooted index heapify."""
		max_index = index
		left_index = self._left_child(index)
		if left_index < self.heap_size:
			max_index = left_index if self.elements[left_index] > self.elements[index] else max_index
		right_index = self._right_child(index)
		if right_index < self.heap_size:
			max_index = right_index if self.elements[right_index] > self.elements[max_index] else max_index
		if max_index != index:
			self.elements[index], self.elements[max_index] = self.elements[max_index], self.elements[index]
			self.max_heapify(max_index)

	def heap_sort(self):
		heap_size = self.heap_size
		while self.heap_size:
			self.elements[0], self.elements[self.heap_size-1] = self.elements[self.heap_size-1], self.elements[0]
			self.heap_size -= 1
			self.max_heapify(0)
		self.heap_size = heap_size

	def _parent(self, index):
		return int((index-1) / 2)

	def _left_child(self, index):
		return 2*index + 1

	def _right_child(self, index):
		return 2*index + 2


if __name__ == '__main__':
	nums = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	heap = MaxHeap(nums)
	heap.heap_sort()
	print(heap.elements)
