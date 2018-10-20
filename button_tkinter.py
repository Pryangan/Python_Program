from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def showRed():
    print("button 1")

def showBlue():
    print("button 2")

def showGreen():
    print("button 3")

def showPurple():
    print("button 4");

button1 = Button(topFrame,text="Button 1",fg="red",command=showRed)
button2 = Button(topFrame,text="Button 2",fg="blue",command=showBlue)
button3 = Button(topFrame,text="Button 3",fg="green",command=showGreen)
button4 = Button(bottomFrame,text="Button 4",fg="purple",command=showPurple)
button5 = Button(bottomFrame,text="Quit",fg="black",command=quit)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
button5.pack(side=BOTTOM)

root.mainloop()
