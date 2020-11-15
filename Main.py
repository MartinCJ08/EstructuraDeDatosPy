import tkinter
import random
from tkinter import *
from Queue import Queue

class Window: 
    def __init__(self):
        random.seed()
        self.myQueue = Queue()

        self.mainWindow = tkinter.Tk()

        self.mainWindow.config(bg ="white")
        self.mainWindow.geometry("600x550")

        self.canvas= Canvas(width =600, height =400, bg ="gray")
        self.btnQueue = Button(self.mainWindow,text ="Queue", command = lambda: self.drawNode(0))
        #self.btnDequeue = Button(self.mainWindow,text ="Dequeue", command = lambda: self.drawNode(1))


        self.btnQueue.pack()
        #self.btnDequeue.pack()
        self.canvas.bind("<ButtonPress-1>", self.onPressKeyboard)
        self.canvas.bind("<ButtonPress-3>", self.onPressKeyboard)
        self.canvas.pack()

        self.currentHeight = self.canvas.winfo_reqheight() - 17
        self.currentWidth = self.canvas.winfo_reqwidth() - 17

        tkinter.mainloop()

    def drawNode(self, pDequeue):
        myVal = random.randint(50,100)
        self.myQueue.enqueue(myVal)

        if pDequeue == 1:
            pass
        self.canvas.create_rectangle(300,300,300,300)

        self.canvas.create_text((300, self.currentHeight), text=str(myVal), font=('Helvetica italic bold', 14), fill='darkblue')
        self.currentHeight = self.currentHeight - 17 

    def onPressKeyboard(self, event):
        print('ALV compa')
        print(event)
        if event.num == 1:
            self.drawNode(0)
        else:
            # TODO: drawNode(1) 
            pass 
        return 'break'

# main method 
if __name__ == "__main__": 
    myGui = Window()