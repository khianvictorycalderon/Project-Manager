# Main entry point of the program, run this .py file
from tkinter import *
import customtkinter as ctk

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")
app.iconbitmap("./Icons/PJM_Full.ico")
app.title("Project Manager")

app.mainloop()