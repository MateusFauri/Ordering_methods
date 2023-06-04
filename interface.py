import os
from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        self.window = ttk.Frame(master, padding=10)
        self.window.grid()

        #self.searchWindow = ttk.Frame(self.window, padding=30)
        #self.searchWindow.grid()

        self.name = Label(self.window, text="File name", font=self.fontePadrao)
        self.name.grid(column=0,row=0, padx=5, pady=3)
        self.path = Entry(self.window, width = 30, font=self.fontePadrao)
        self.path.grid(column=1,row=0, padx=5, pady=3)
        self.search = Button(self.window, text="Search", font=("Calibri", "8"), width=12, command=self._searchFile)
        self.search.grid(column=1,row=1, padx=5, pady=3)
        self.message = Label(self.window, text="", font=self.fontePadrao)
        self.message.grid(column=1,row=2, padx=5, pady=3)

        methodOptions = ["Selection", "Insertion", "Shell", "Heap"]
        self.clicked = StringVar()
        self.clicked.set("Heap")

        self.methodLabel = Label(self.window, text="Method for sorting", font=self.fontePadrao)
        self.methodLabel.grid(column=0, row=3, padx=5, pady=3)
        self.method = OptionMenu(self.window, self.clicked, *methodOptions)
        self.method.grid(column=1, row=3, padx=5, pady=3)

        self.exit = ttk.Button(self.window, text="Quit", command=master.destroy, width=5)
        self.exit.grid(column=6, row=10, padx=5, pady=3)

    def _searchFile(self):
        fileName = self.path.get()
        fileName = fileName + '.txt'
        try:
            self._file = open(fileName,'r')
            self.message["text"] = "File found!"
        except:
            self.message["text"] = "Can't reed this file."

    def _getList(self):
        self.list = []
        self.size = 0 
        line = self._file.readline()

        self.size = line[0]
        self.list = line[1:]

        if self.list[-1] == '\n':
            self.list.pop(-1)

    def _sort(self):
        pass

def interfaceTtk():
    root = Tk()

    #root.geometry("800x500")
    root.title("Sort List")
    root.config(bg="#aad5df")

    Application(root)
    root.mainloop()

def desenhar_interface():
    print("*"*40)
    print("\t1 - Insertion sort")
    print("\t2 - Shell sort")
    print("\t3 - Selection sort")
    print("\t4 - Heap sort")
    print("\t0 - Sair")
    print("*"*40)
    selecao = int(input("Selecione a ordenação:  "))

    while selecao < 0 and selecao > 4:
        print("Numero invalido! Tente novamente.")
        selecao = int(input("Selecione a ordenação:  "))

    return selecao
        
def selection_sort_interface():
    print("*"*20)
    print("\t1 - SHELL")
    print("\t2 - Knuth")
    print("\t3 - Ciura")
    print("*"*20)
    gap = int(input("Selecione a lista de gaps:  "))

    while gap < 1 and gap > 3:
        print("Numero invalido! Tente novamente.")
        gap = int(input("Selecione a lista de gaps:  "))

    if gap == 1:
        return "SHELL"
    elif gap == 2:
        return 'KNUTH'
    else:
        return "CIURA"