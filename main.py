# Main entry point of the program, run this .py file
from tkinter import *
import customtkinter as ctk

from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4
from dual_frame import create_dual_frame

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")
app.iconbitmap("./Icons/PJM_Full.ico")
app.title("Project Manager")

frame_content = {
    "Project Management": {
        "Add Project": lambda _: print(),
        "Edit Project": lambda _: print(),
        "View and Delete Project": lambda _: print()
    }
}

dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color=color_1, right_frame_bg_color=color_2, button_hover_color=color_3, left_frame_font=font_3)
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()