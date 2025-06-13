from tkinter import *
import customtkinter as ctk
from tkinter import messagebox

# Defaults
from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4
from global_var import * # db_path

# Templates
from ctk_temp_entry_dropdown_mixed_input import create_entry_dropdown
from opxl_temp_update import opxl_update

def edit_project_page(parent):
    ctk.CTkLabel(parent, text="Edit Project", font=font_1).pack(pady=20)

    edit_project_vars = {}
    edit_project_fields = {
        "Project ID": "text",
        "Update Field": edit_update_field,
        "New Value": "text"
    }

    def edit_project():

        # Get the variables
        project_id = edit_project_vars["Project ID"].get()
        project_update_field = edit_project_vars["Update Field"].get()
        project_new_value = edit_project_vars["New Value"].get()

        try:

            # Update new value
            opxl_update(db_path, project_sheet, new_values={project_update_field: project_new_value}, condition={"ID": project_id})

            # Clears the input
            for item in edit_project_vars.values():
                item.set("")
            edit_project_vars["Update Field"].set(edit_update_field[0]) # Set the value to the initial for dropdown

            # Message
            messagebox.showinfo("Update Success", "Successfully updated new data!")

        except Exception as error:
            messagebox.showerror("Update Failed", f"Unable to update data: {error}")

    create_entry_dropdown(
        parent, 
        edit_project_fields, 
        col_per_rows=1, 
        input_bg_color=color_6,
        input_text_color=color_1,
        variable=edit_project_vars,
        button_color=color_3,
        button_hover_color=color_4,
        button_label="Edit Project",
        default_font=font_3,
        on_submit=edit_project
    ).pack(fill = BOTH)