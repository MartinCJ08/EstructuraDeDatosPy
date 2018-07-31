class QueueNode:
	"""docstring for QueueNode"""
	def __init__(self):
		self.data = None
		self.prev = None

	def getData(self):
		return self.data
	def setData(self,data):
		self.data = data
	def getPrev(self):
		return self.prev
	def setPrev(self,prev):
		self.prev = prev
		