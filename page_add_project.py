from tkinter import *
import customtkinter as ctk
from tkinter import messagebox

# Defaults
from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4
from global_var import * # db_path

# Templates
from ctk_temp_entry_dropdown_mixed_input import create_entry_dropdown
from opxl_temp_insert import opxl_insert
from opxl_temp_unique_id import generate_unique_id_across_sheets

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
        
        # Get input variables
        project_id = generate_unique_id_across_sheets(db_path, sheets_name=[project_sheet])
        project_name = add_project_vars["Name"].get()
        project_description = add_project_vars["Description"].get()
        project_date_start = add_project_vars["Date Started"].get()
        project_date_finished = add_project_vars["Date Finished"].get()
        project_remarks = add_project_vars["Remarks"].get()

        try:
            insert_data = [project_id, project_name, project_description, project_date_start, project_date_finished, project_remarks]
            opxl_insert(db_path, project_sheet, data=insert_data)
            
            # Clears the input
            for item in add_project_vars.values():
                item.set("")
            
            messagebox.showinfo("Add Success", f"Project {project_name} successfully added!")

        except Exception as error:
            messagebox.showerror("Add Failed",f"Unable to add project: {error}")

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