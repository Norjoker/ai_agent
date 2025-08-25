import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        print(full_path)
        print(working_directory)

        if not os.path.isfile(os.path.abspath(full_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        elif os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"