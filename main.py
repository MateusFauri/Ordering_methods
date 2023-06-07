import interfaces.windows as windows
import customtkinter as ctk
from tkinter import *

class CTkApplication(ctk.CTk):
    def __init__(self, master=None):
        self.frame = windows.MainInterface(master)

        self.exit = ctk.CTkButton(master, text="Quit", command=master.destroy)
        self.exit.grid(column=1, row=10, padx=15, pady=10)

def interfaceCTk():
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()  
    app.title("Sorting")
    
    CTkApplication(app)

    app.mainloop()

interfaceCTk()

