from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import os
import tkinter.font as tkFont
from tkinter import ttk
import pyperclip
import pyautogui,datetime
class font():
    def __init__(self,master,text):
        self.text=text
        self.root=Toplevel(master)
        self.root.minsize(499,349)
        self.root.maxsize(500,350)
        self.root.title("Font")
        self.lab =ttk.Label(self.root,text="Font",font=("Arial",10))
        self.lab.place(x=10,y=0)
        self.familyC=StringVar()
        self.combo=ttk.Combobox(self.root,textvariable=self.familyC)
        self.combo['values']=tuple(tkFont.families())
        self.combo.current(0)
        self.combo.place(x=60,y=1)
        self.lab1 = ttk.Label(self.root,text="Font Style", font=("Arial", 10))
        self.lab1.place(x=10, y=50)
        self.StyleC = StringVar()
        self.combo1 = ttk.Combobox(self.root, textvariable=self.StyleC)
        self.combo1['values'] = ("normal","bold")
        self.combo1.current(0)
        self.combo1.place(x=100, y=50)
        self.lab2 = ttk.Label(self.root, text="Font Size", font=("Arial", 10))
        self.lab2.place(x=10, y=100)
        self.SizeC = StringVar()
        self.combo2 = ttk.Combobox(self.root, textvariable=self.SizeC)
        self.combo2['values'] = tuple(range(4,50))
        self.combo2.current(0)
        self.combo2.place(x=100, y=100)
        self.but1=Button(self.root,text="OK",command=self.update)
        self.but1.place(x=300, y=300)
        self.but2 = Button(self.root, text="Cancel",command=self.dest)
        self.but2.place(x=350, y=300)
    def dest(self):
        self.root.destroy()
    def update(self):
        family=self.combo.get()
        weight=self.combo1.get()
        size=self.combo2.get()
        Font = tkFont.Font(family=self.combo.get(), weight=self.combo1.get(),size=self.combo2.get())
        self.text.configure(font=Font)
        self.root.destroy()
class window(Tk):
    ls=[]
    def __init__(self):
        super(window,self).__init__()
        self.open=False
        self.geometry("1000x800")
        self.title("Notepad")
        self.configure(background="white")
        self.but=Button(self,text="create a new file",font=("arial",40),bg="white",command=self.new_file)
        self.but.pack()
        self.lab=Label(self,text="or",bg="white",font=("arial",40))
        self.lab.pack()
        self.but1 = Button(self, text="open an existing one", font=("arial", 40),bg="white",command=self.create)
        self.but1.pack()
    def addFontClass(self):
        f=font(self,self.scroll)
    def createScroll(self):
        self.scroll = Text(self, undo=True)
        self.scroll.pack(expand=True, fill=BOTH)
    def create(self):
        self.but.destroy()
        self.lab.destroy()
        self.but1.destroy()
        self.createScroll()
        self.file=filedialog.askopenfilename(initialdir="/",title="Open File",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
        try:
            self.create_menu()
            self.scroll.delete(1.0, END)
            file=open(self.file,"r")
            self.scroll.insert(1.0,file.read())
            self.lab.destroy()
            self.title(os.path.basename(self.file) + "-Notepad")
            file.close()
        except:
            print("you did not open any file")
            self.title("untitled Notepad")
        self.file_menu.entryconfigure(0, state=NORMAL)
        self.open=True
    def killMe(self):
        self.destroy()
        self.quit()
    def new_file(self):
        if self.open==True:
            self.scroll.delete(1.0, END)
        self.title("untitled Notepad")
        self.createScroll()
        file=None
        try:
            self.scroll.delete(1.0,END)
            self.but.destroy()
            self.lab.destroy()
            self.but1.destroy()
        except:
            print("new file")
        self.create_menu()
        self.file_menu.entryconfigure(0,state=DISABLED)
    def save(self):
        try:
            self.file=filedialog.asksaveasfile(title="save",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
            self.title(os.path.basename(self.file)+"-Notepad")
            self.file_menu.entryconfigure(2, state=DISABLED)
            saved=True
        except:
            print("you did not save")
    def saveas(self):
        try:
            self.file=filedialog.asksaveasfile(filetypes=(("Text Files","*.txt"),("All Files","*.*")))
            self.title(os.path.basename(self.file)+"-Notepad")
            saved=True
        except:
            print("you did not save")
    def selCut(self):
        try:
            self.scroll.delete(SEL_FIRST,SEL_LAST)
        except:
            print("something is wrong")
    def selCopy(self):
        try:
            pyperclip.copy(self.scroll.selection_get())
        except:
            print("something is wrong")
    def selPaste(self):
        try:
            pyperclip.paste()
        except:
            print("something is wrong")
    def create_menu(self):
        menuBar=Menu(self)
        self.config(menu=menuBar)
        self.file_menu=Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New",command=self.new_file)
        self.file_menu.add_command(label="Open",command=self.create)
        self.file_menu.add_command(label="Save",command=self.save)
        self.file_menu.add_command(label="Save as",command=self.saveas)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.killMe)
        Edit_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=Edit_menu)
        Edit_menu.add_command(label="Undo",command=self.scroll.edit_undo)
        Edit_menu.add_command(label="Redo",command=self.scroll.edit_redo)
        Edit_menu.add_separator()
        Edit_menu.add_command(label="Cut",command=self.selCut)
        Edit_menu.add_command(label="Copy",command=self.selCopy)
        Edit_menu.add_command(label="Paste",command=self.selPaste)
        Edit_menu.add_command(label="Delete",command=self.selCut)
        Edit_menu.add_separator()
        Edit_menu.add_command(label="Select All",command=lambda *awargs:pyautogui.hotkey("ctrl","a"))
        font_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Format", menu=font_menu)
        font_menu.add_command(label="Font", command=self.addFontClass)
if __name__ == "__main__":
    win=window()
    win.mainloop()