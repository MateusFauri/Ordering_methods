from tkinter import *
import customtkinter as ctk
from sort import *
import os
import time

def interfaceCTk():
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()  
    app.title("Sorting")
    
    CTkApplication(app)

    app.mainloop()


class CTkApplication(ctk.CTk):
    def __init__(self, master=None):

        self.frame = ctk.CTkFrame(master=master)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.path = ctk.CTkEntry(self.frame, width = 200, placeholder_text="File name")
        self.path.grid(column=0,row=1, padx=15, pady=10)
        self.search = ctk.CTkButton(self.frame, text="Search", command=self._searchFile)
        self.search.grid(column=0,row=2, padx=15, pady=10)
        self.message = ctk.CTkLabel(self.frame, text="", fg_color="transparent")
        self.message.grid(column=0,row=3, padx=3, pady=3)

        methodOptions = ["Heap", "Selection", "Insertion", "Shell"]

        self.methodLabel = ctk.CTkLabel(self.frame, text="Method for sorting", fg_color="transparent")
        self.methodLabel.grid(column=0,row=4, padx=3, pady=3)
        self.method = ctk.CTkOptionMenu(self.frame, values=methodOptions)
        self.method.grid(column=0,row=5, padx=15, pady=10)

        self.order = ctk.CTkButton(self.frame, text="Order list", command=self._sort, state="disabled")
        self.order.grid(column=0, row=6, padx=15, pady=10)

        self.exit = ctk.CTkButton(self.frame, text="Quit", command=master.destroy)
        self.exit.grid(column=0, row=10, padx=15, pady=10)

    def _searchFile(self):
        fileName = self.path.get()
        fileName = fileName + '.txt'
        try:
            self._file = open(fileName,'r')
            self.message.configure(text="File found!") 
            self._getList()
            self._activateSort()
        except:
            self.message.configure(text="Can't reed this file.")

    def _activateSort(self):
        self.order.configure(state="normal")

    def _getList(self):
        self.list = []
        self.size = 0 
        line = self._file.readline().split()

        self.size = int(line[0])
        self.list = line[1:]
        if self.list[-1] == '\n':
            self.list.pop(-1)

        self.list = list(map(lambda x: int(x), self.list))

        self._file.close()

    def _sort(self):
        sort = sorts(self.list, self.size)
        method = self.clicked.get()
        inicio = time.time()

        if method == "Selection":
            sort.selection_sort()
        elif method == "Heap":
            sort.heap_sort()
        elif method == "Insertion":
            sort.insertionSort(solo=True)
        elif method == "Shell":
            sort.shell_sort()
        fim = time.time()

        with open('saida.txt','w') as saida:
            for element in self.list:
                saida.write(str(element) + ' ')
    
            saida.write(f"\nTempo: {fim-inicio:.6f} segundos com tamanho {self.size} elementos.")
        