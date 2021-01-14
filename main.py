# create a single window
#   and a widget in the window

import tkinter as tk

# create window as instnace of the TK class
window = tk.Tk()

# create a frame
navBar = tk.Frame()
navBar.pack()

textBox = tk.Frame()
textBox.pack()

# labels for nav
newFile = tk.Label(text="New", master=navBar)
newFile.pack()

openFile = tk.Label(text="Open", master=navBar)
openFile.pack()

saveFile = tk.Label(text="Save", master=navBar)
saveFile.pack()

deleteFile = tk.Label(text="Delete", master=navBar)
deleteFile.pack()

copyFile = tk.Label(text="Copy", master=navBar)
copyFile.pack()

cutFromFile = tk.Label(text="Cut", master=navBar)
cutFromFile.pack()

pasteOn = tk.Label(text="Paste", master=navBar)
pasteOn.pack()

window.mainloop()
