import copy


class Heap:

	def __init__(self, array=[]):
		self.heap_list = array

	def heapify(self):
		length = len(self.heap_list)
		for i in range(length-1, -1, -1):
			self.sift_down(i)

	def sift_down(self, index):
		length = len(self.heap_list)
		left_index = 2*index + 1
		right_index = 2*index + 2

		if left_index >= length:
			return

		min_index = copy.deepcopy(index)

		if self.heap_list[index] > self.heap_list[left_index]:
			min_index = left_index

		if right_index < length and self.heap_list[min_index] > self.heap_list[right_index]:
			min_index = right_index

		if min_index != index:
			temp = self.heap_list[index]
			self.heap_list[index] = self.heap_list[min_index]
			self.heap_list[min_index] = temp
			self.sift_down(min_index)

	def insert(self, x):
		length = len(self.heap_list)
		self.heap_list.append(x)
		self.sift_up(length)

	def sift_up(self, index):
		if index != 0:
			parent_index = (index - 1) / 2
			if self.heap_list[parent_index] > self.heap_list[index]:
				temp = self.heap_list[parent_index]
				self.heap_list[parent_index] = self.heap_list[index]
				self.heap_list[index] = temp
				self.sift_up(parent_index)

	def delete_min(self):
		length = len(self.heap_list)

		if length == 0:
			return
		else:
			self.heap_list[0] = self.heap_list[length - 1]
			self.heap_list.pop()
			self.sift_down(0)


h = Heap()
h.insert(10)
h.insert(9)
h.insert(8)
h.insert(1)
h.insert(7)
h.insert(2)
h.delete_min()
h.insert(3)
h.insert(8)
h.insert(1)
h.delete_min()

