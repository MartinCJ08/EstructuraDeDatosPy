from Node import *

class Stack:
	def __init__(self):
		self.top = None
	def push(self,data):
		if self.top == None:
			self.top = Node()
			self.top.setData(data)
		else:
			temp = Node()
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