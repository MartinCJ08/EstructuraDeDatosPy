from QueueNode import *
from StructureData import * 

class Queue(StructureData):
	front = None

	def __init(self):
		self.front = None
		self.back = None
	def enqueue(self,data):
		#add an element to the queue
		if self.front == None:
			self.front = QueueNode()
			self.front.setData(data)
			self.back = self.front
		else:
			self.temp = QueueNode()
			self.temp.setData(data)
			self.back.setPrev(self.temp)
			self.back = self.temp
			self.temp = None
		
	def dequeue(self):
		#remove the first element from the queue
		if not self.front == None:
			data = self.front.getData()
			temp = self.front.getPrev()
			self.front = temp
			temp = None
			
		return data

	def print(self):
		# super(Queue, self).print() # Manera de imprimir el concepto 
		node = self.front
		while node != None:
			print(node.getData())
			node = node.getPrev()