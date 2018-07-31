from Stack import *
from Queue import *

def main():
	myStack = Stack()
	myStack.push(60)
	myStack.push(30)
	myStack.push(20)
	myStack.print()
	myStack.pop()
	print("Pop")
	myStack.print()	
	myQueue = Queue()
	myQueue.enqueue(3)
	myQueue.enqueue(4)
	myQueue.enqueue(5)
	myQueue.enqueue(6)
	myQueue.enqueue(7)

if __name__ == '__main__':
	main()