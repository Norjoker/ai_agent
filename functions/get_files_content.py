import os
from config import MAX_CHARS
from google.genai import types

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

schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Gets content of a specified file in string format, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from which to read, relative to the working directory.",
            ),
        },
    ),
)