import os
from config import MAX_CHARS
from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites file specified in file path or creates a new file if nonexistent, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from which to write/create, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The new text to overwrite the existing file with or to add to the newly created file.",
            ),
        },
    ),
)