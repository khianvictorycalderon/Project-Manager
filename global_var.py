import os

db_path = os.path.join(os.environ["PUBLIC"], "KV-Project-Manager-Data", "data.xlsx")

project_sheet_headers = ["ID", "Name", "Description", "Date Started", "Date Finished", "Remarks"]
project_sheet = "Projects"