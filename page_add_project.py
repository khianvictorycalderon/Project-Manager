from tkinter import *
import customtkinter as ctk

# Defaults
from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4

# Templates
from ctk_temp_entry_dropdown_mixed_input import create_entry_dropdown

def add_project_page(parent):
    ctk.CTkLabel(parent, text="Add Project", font=font_1).pack(pady=20)

    add_project_vars = {}
    add_project_fields = {
        "Name": "text",
        "Description": "text",
        "Date Started": "text",
        "Date Finished": "text",
        "Remarks": "text"
    }

    def add_project():
        pass

    create_entry_dropdown(
        parent, 
        add_project_fields, 
        col_per_rows=1, 
        input_bg_color=color_6,
        input_text_color=color_1,
        variable=add_project_vars,
        button_color=color_3,
        button_hover_color=color_4,
        button_label="Add Project",
        default_font=font_3,
        on_submit=add_project
    ).pack(fill = BOTH)