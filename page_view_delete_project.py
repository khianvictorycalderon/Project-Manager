from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import pyperclip

# Defaults
from colors import * # color_1, color_2, up to color_6
from fonts import * # font_1, font_2, up to font_4
from global_var import * # db_path

# Templates
from ctk_temp_treeview import create_treeview
from opxl_temp_read import opxl_read
from opxl_temp_delete import opxl_delete

def view_delete_project_page(parent):

    # Read the actual projects
    project_list = opxl_read(db_path, project_sheet)
    if not len(project_list) > 0:
        ctk.CTkLabel(parent, text="You don't have a projects yet.", font=font_1).pack(pady=50)
        return
    
    # Main title
    ctk.CTkLabel(parent, text="View & Delete Project", font=font_1).pack(pady=20)

    def copy_id(data):
        try:
            pyperclip.copy(data[0]) # Copy the ID
        except Exception as error:
            messagebox.showerror("Failed to Copy", f"Unable to Copy: {error}")

    def delete_item(data):
        delete_id = data[0]
        delete_name = data[1]

        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete project {delete_name}?"):
            return

        try:
            opxl_delete(db_path, project_sheet, condition={"ID": delete_id})
            refresh_tree()
            messagebox.showinfo("Delete Success", f"Project {delete_name} successfully deleted!")
        except Exception as error:
            messagebox.showerror("Failed to Delete", f"Unable to Delete: {error}")

    tree_buttons = {
        "Copy ID": {"📜": copy_id},
        "Delete Item": {"⛔": delete_item}
    }

    tree = ctk.CTkFrame(parent)
    def refresh_tree():
        nonlocal tree
        tree.destroy()
        updated_list = opxl_read(db_path, project_sheet)

        tree = create_treeview(
            parent,
            action_buttons=tree_buttons, 
            columns=project_sheet_headers, 
            data=updated_list[::-1],
            content_bg=color_2,
            text_color=color_6,
            font=font_4,
            row_a_bg=color_2,
            row_b_bg=color_1,
            header_bg_color=color_1,
            header_text_color=color_6,
            search_label="Search for: ",
            search_box_bg_color=color_6,
            search_box_text_color=color_1,
            dropdown_bg_color=color_6,
            dropdown_text_color=color_1,
        )
        tree.pack(fill=BOTH)

    refresh_tree()