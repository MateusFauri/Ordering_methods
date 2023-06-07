import customtkinter as ctk
from tkinter import *
from metodos.sort import *
import os

class MainInterface(ctk.CTk):
    def __init__(self, master=None):
        self.frame = ctk.CTkFrame(master)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.resultFrame = ResultFrame(master)

        self.path = ctk.CTkEntry(self.frame, width = 200, placeholder_text="File name")
        self.path.grid(column=0,row=1, padx=15, pady=10)
        self.search = ctk.CTkButton(self.frame, text="Search", command=self._searchFile)
        self.search.grid(column=0,row=2, padx=15, pady=10)
        self.message = ctk.CTkLabel(self.frame, text="", fg_color="transparent")
        self.message.grid(column=0,row=3, padx=3, pady=3)

        methodOptions = ["Quick", "Selection", "Insertion", "Shell", "Heap"]

        self.methodLabel = ctk.CTkLabel(self.frame, text="Method for sorting", fg_color="transparent")
        self.methodLabel.grid(column=0,row=4, padx=3, pady=3)
        self.method = ctk.CTkOptionMenu(self.frame, values=methodOptions)
        self.method.grid(column=0,row=5, padx=15, pady=10)

        self.order = ctk.CTkButton(self.frame, text="Order list", command=self._sort, state="disabled")
        self.order.grid(column=0, row=6, padx=15, pady=10)
        self._counting = 0


    def _searchFile(self):
        fileName = self.path.get()
        fileName = os.path.join(os.getcwd() , 'arquivos', fileName + '.txt')
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
        method = self.method.get()
        self.resultFrame.frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.resultFrame.sorting()

        inicio = time.time()
        
        if method == "Selection":
            sort.selection_sort()
        elif method == "Heap":
            sort.heap_sort()
        elif method == "Insertion":
            sort.insertionSort(solo=True)
        elif method == "Shell":
            sort.shell_sort()
        elif method == "Quick":
            sort.quick_sort()
        
        fim = time.time()

        self.resultFrame.doneSort()
        self.resultFrame.time(fim-inicio)
        fileName = 'saida' + str(self._counting)
        saida = os.path.join(os.getcwd(), 'arquivos', fileName + '.txt')
        with open(saida,'w') as saida:
            for element in self.list:
                saida.write(str(element) + ' ')
    
            saida.write(f"\nTempo: {fim-inicio:.6f} segundos com tamanho {self.size} elementos com metodo {method}.")

        self._counting += 1

class ResultFrame(ctk.CTkFrame):
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master, width=50, height=50)
        self.resultTime = ctk.CTkLabel(self.frame, text="", fg_color="transparent")
        self.done = ctk.CTkLabel(self.frame, text="", fg_color="transparent")

    def sorting(self):
        self.done.grid(row=0, column=1)
        self.done.configure(text="Sorting....")

    def doneSort(self):
        self.done.configure(text="Finish!")

    def time(self, time):
        self.resultTime.grid(row=4, column=1)
        self.resultTime.configure(text=f"Time: {time:.6f} seconds. ")
