import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        input = ["python3",full_path]
        if args != None:
            input.extend(args)

        #print(f"Trying to run: {full_path}")
        #print(working_directory)

        if not os.path.isfile(os.path.abspath(full_path)):
            return f'Error: File "{file_path}" not found.'
        elif not (os.path.abspath(full_path)).endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        elif os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        result = subprocess.run(input, timeout=30, capture_output=True, check=True, text=True)
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"

        stdout, stderr = result.stdout, result.stderr
        if stdout == None:
            return "No output produced"

        return f"STDOUT: {stdout}\nSTDERR: {stderr}"

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified file with any optional args, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="List of optional arguments to pass to the function",
            ),
        },
    ),
)