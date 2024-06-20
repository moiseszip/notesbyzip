import tkinter as tk
from tkinter import *
from tkinter import ttk

#set root as a Tk object
root = tk.Tk()

#set title and frame size
root.title("Notes by Zip")
root.geometry("800x600")

#set menu bar
menuBar = tk.Menu(root)
root.config(menu=menuBar)

#file cascade
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

#edit cascade
editMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)



root.mainloop()