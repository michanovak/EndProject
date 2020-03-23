from tkinter import *
from tkinter import messagebox


def newFile():
    messagebox.showinfo(LABEL, 'New File')

def openFile():
    messagebox.showinfo(LABEL, 'Open File')

def exit_app():
    messagebox.showinfo(LABEL, 'Good Bye')
    root.quit()

def about():
    messagebox.showinfo(LABEL, 'Designd By Micha')







root = Tk()

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Exit", command=exit)

help_menu = Menu(menu)
menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_cascade(label="About",command=about)
checkboxVar1 = IntVar()

root.config(menu=menu)

root.grid()

root.title("Portal")
root.minsize(600, 500)
root.maxsize(900, 900)
root.resizable(width=False, height=False)
root.configure(bg="#4c9bd4")

#login = Button(root, text="Login", height="0", width="20", command=login)
#login.grid(row=1, column=0, padx=(10, 0), pady=(20, 0))

#register = Button(root, text="Register", height="0", width="20", command=register)
#register.grid(row=1, column=3, padx=(350, 0), pady=(20, 0))

root.mainloop()