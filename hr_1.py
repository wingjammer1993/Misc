class LRUCache:
	def __init__(self, cap):
		"""
		:type capacity: int
		"""
		self.capacity = cap
		self.usage = []
		self.cache = {}

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		self.usage.insert(key, 0)
		if len(self.usage) >= self.capacity:
			self.usage = self.usage[0:self.capacity]

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: void
		"""
		self.cache[key] = value
		if self.capacity < len(self.cache):
			self.cache.pop(self.usage[-1])


			# Your LRUCache object will be instantiated and called as such:
			# obj = LRUCache(capacity)
			# param_1 = obj.get(key)
			# obj.put(key,value)