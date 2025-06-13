# Main entry point of the program, run this .py file
from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import sys

# Defaults
from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4
from global_var import * # db_path

# Templates
from opxl_temp_ensures import * # ensure_excel_exist, ensure_sheet_exist, and remove_sheet
from opxl_temp_headers import opxl_write_headers
from ctk_temp_dual_frame import create_dual_frame

# Pages
from page_add_project import add_project_page
from page_edit_project import edit_project_page
from page_view_delete_project import view_delete_project_page
from page_credits import credits_page

app = ctk.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")
app.iconbitmap("./Icons/PJM_Full.ico")
app.title("Project Manager")

# Ensure that everything works correctly:
ensure_excel_exist(db_path)
ensure_sheet_exist(db_path, project_sheet)
project_sheet_headers = ["ID", "Name", "Description", "Date Started", "Date Finished", "Remarks"]
opxl_write_headers(db_path, project_sheet, headers=project_sheet_headers)
remove_sheet(db_path, sheet_name="Sheet") # Remove default sheet

frame_content = {
    "Project Management": {
        "Add Project": add_project_page,
        "Edit Project": edit_project_page,
        "View and Delete Project": view_delete_project_page,
    },
    "Misc": {
        "Credits": credits_page,
        "Exit": lambda _: sys.exit()
    }
}

dual_frame = create_dual_frame(app, frame_content, left_frame_bg_color=color_1, right_frame_bg_color=color_2, button_hover_color=color_3, left_frame_font=font_3)
dual_frame.pack(expand = True, fill = BOTH)

app.mainloop()