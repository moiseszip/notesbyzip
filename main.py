import tkinter as tk
from tkinter import *
from tkinter import filedialog, font, colorchooser
from tkinter import ttk

#set root as a Tk object
root = tk.Tk()

#set title frame and size
root.title("Untitled - Notes by Zip")
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

#set file address to none
filePath = None

#file menu functions
#from line 1 column 0 to END
def newFile(event=None):
    textArea.delete(1.0, tk.END)
    updateTitle()

#open .txt files
def openFile(event=None):
    global filePath
    filePath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    #read file, clear textArea, then insert read file
    if filePath:
        with open(filePath, "r") as file:
            textArea.delete(1.0, tk.END)
            textArea.insert(tk.END, file.read())

    updateTitle()

#save text in the same address
def saveFile(event=None):
    global filePath
    if filePath:
        with open(filePath, "w") as file:
            file.write(textArea.get(1.0, tk.END))
    else:
        saveAsFile()

    updateTitle()

#save text as .txt (open file explorer)
def saveAsFile(event=None):
    global filePath
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    #write in file text from line 1, column 0 to END
    if filePath:
        with open(filePath, "w") as file:
            file.write(textArea.get(1.0, tk.END))

    updateTitle()

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
def undo(event=None):
    textArea.edit_undo()

def copy(event=None):
    textArea.event_generate("<<Copy>>")

def cut(event=None):
    textArea.event_generate("<<Cut>>")

def paste(event=None):
    textArea.event_generate("<<Paste>>")

#set edit menu function labels
editMenu.add_command(label="Undo (Ctrl+Z)", command=undo)
editMenu.add_command(label="Copy (Ctrl+C)", command=copy)
editMenu.add_command(label="Cut (Ctrl+X)", command=cut)
editMenu.add_command(label="Paste (Ctrl+V)", command=paste)

#style functions
def toggleBold(event=None):
    currentStyle = textArea.tag_names("sel.first")
    if "bold" in currentStyle:
        textArea.tag_remove("bold", "sel.first", "sel.last")
    else:
        textArea.tag_add("bold", "sel.first", "sel.last")
        boldFont = font.Font(textArea, textArea.cget("font"))
        boldFont.configure(weight="bold")
        textArea.tag_configure("bold", font=boldFont)

def toggleUnderline(event=None):
    currentStyle = textArea.tag_names("sel.first")
    if "underline" in currentStyle:
        textArea.tag_remove("underline", "sel.first", "sel.last")
    else:
        textArea.tag_add("underline", "sel.first", "sel.last")
        underlineFont = font.Font(textArea, textArea.cget("font"))
        underlineFont.configure(underline=True)
        textArea.tag_configure("underline", font=underlineFont)

def toggleItalic(event=None):
    try:
        currentStyle = textArea.tag_names("sel.first")
        if "italic" in currentStyle:
            textArea.tag_remove("italic", "sel.first", "sel.last")
        else:
            textArea.tag_add("italic", "sel.first", "sel.last")
            italicFont = font.Font(textArea, textArea.cget("font"))
            italicFont.configure(slant="italic")
            textArea.tag_configure("italic", font=italicFont)
    except tk.TclError:
        pass

#testing style buttons on footer
boldButton = ttk.Button(root, text="B", command=toggleBold, width=3)
boldButton.pack(side="left")

underlineButton = ttk.Button(root, text="U", command=toggleUnderline, width=3)
underlineButton.pack(side="left")

italicButton = ttk.Button(root, text="I", command=toggleItalic, width=3)
italicButton.pack(side="left")

#color picker
def chooseFontColor():
    global color
    color = colorchooser.askcolor()[1]
    if color:
        textArea.tag_add("font_color", "sel.first", "sel.last")
        textArea.tag_configure("font_color", foreground=color)

def chooseBgColor():
    global color
    color = colorchooser.askcolor()[1]
    if color:
        textArea.tag_add("background_color", "sel.first", "sel.last")
        textArea.tag_configure("background_color", background=color)

fontColorButton = ttk.Button(root, text="Font Color", command=chooseFontColor)
fontColorButton.pack(side="left")

bgColorButton = ttk.Button(root, text="BG Color", command=chooseBgColor)
bgColorButton.pack(side="left")

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
root.bind("<Control-b>", toggleBold)

#update title based on file's name
def updateTitle():
    global filePath
    if filePath:
        fileName = filePath.split("/")[-1]
        root.title(f"{fileName} - Notes by Zip")
    else:
        root.title("Untitled - Notes by Zip")

updateTitle()
root.mainloop()