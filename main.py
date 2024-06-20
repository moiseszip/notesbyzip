import tkinter as tk
from tkinter import *
from tkinter import filedialog, font, colorchooser
from tkinter import ttk

#set root as a Tk object
root = tk.Tk()

#set title frame and size
root.title("* - Notes by Zip")
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

#set text area
textArea = tk.Text(root, undo=True, wrap="word")
textArea.pack(expand=1, fill="both")

#file menu functions
#from line 1 column 0 to END
def newFile(event=None):
    textArea.delete(1.0, tk.END)

#set file address to none
filePath = None

#open .txt files
def openFile(event=None):
    filePath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    #read file, clear textArea, then insert read file
    if filePath:
        with open(filePath, "r") as file:
            textArea.delete(1.0, tk.END)
            textArea.insert(tk.END, file.read())

#save text in the same address
def saveFile():

    if filePath:
        if filePath:
            with open(filePath, "w") as file:
                file.write(textArea.get(1.0, tk.END))
        else:
            saveAsFile()

#save text as .txt (open file explorer)
def saveAsFile(event=None):
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    #write in file text from line 1, column 0 to END
    if filePath:
        with open(filePath, "w") as file:
            file.write(textArea.get(1.0, tk.END))

#exit
def closeApp(event=None):
    root.quit() 

#set label to file functions
fileMenu.add_command(label="New (Ctrl+N)", command=newFile)
fileMenu.add_command(label="Open (Ctrl+O)", command=openFile)
fileMenu.add_command(label="Save (Ctrl+S)", command=saveFile)
fileMenu.add_command(label="Save As (Ctrl+Shift+S)", command=saveAsFile)
fileMenu.add_command(label="Exit (Ctrl+W)", command=closeApp)

#edit menu functions
def undo():
    textArea.edit_undo()

def copy():
    textArea.event_generate("<<Copy>>")

def cut():
    textArea.event_generate("<<Cut>>")

def paste():
    textArea.event_generate("<<Paste>>")

#set edit menu function labels
editMenu.add_command(label="Undo (Ctrl+Z)", command=undo)
editMenu.add_command(label="Copy (Ctrl+C)", command=copy)
editMenu.add_command(label="Cut (Ctrl+X)", command=cut)
editMenu.add_command(label="Paste (Ctrl+V)", command=paste)

#binds
root.bind("<Control-n>", newFile)
root.bind("<Control-o>", openFile)
root.bind("<Control-s>", saveFile)
root.bind("<Control-Shift-s>", saveFile)
root.bind('<Control-w>', closeApp)
root.bind('<Control-z>', undo)
root.bind('<Control-c>', copy)
root.bind('<Control-x>', cut)
root.bind('<Control-v>', paste)

def updateTitle():
    if filePath:
        fileName = filePath.split("/")[-1]  # Get the base file name
        root.title(f"{fileName} - Notes by Zip")
    else:
        root.title("* - Notes by Zip")

updateTitle()
root.mainloop()