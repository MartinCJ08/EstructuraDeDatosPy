from StackNode import *
from StructureData import *

class Stack(StructureData):
	def __init__(self):
		self.top = None
	def push(self,data):
		if self.top == None:
			self.top = StackNode()
			self.top.setData(data)
		else:
			temp = StackNode()
			temp.setData(data)
			temp.setNext(self.top)
			self.top = temp
		
	def pop(self):
		temp = self.top
		data = self.top.getData()
		self.top = self.top.getNext()
		temp = None
		return data

	def print(self):
		node = self.top
		while node != None:
			print(node.getData())
			node = node.getNext()