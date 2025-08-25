import os
from config import MAX_CHARS

def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        #print(full_path)
        #print(working_directory)

        if os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        with open(full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"