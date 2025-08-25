import os

def get_files_info(working_directory, directory="."):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        #print(full_path)
        #print(working_directory)

        if not os.path.isdir(os.path.abspath(full_path)):
            return f'Error: "{directory}" is not a directory'
        elif os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        content = os.listdir(full_path)
        content_info = ""
        for item in content:
            p = os.path.join(full_path, item)
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            content_info += f"- {item}: file_size={size} bytes, is_dir={is_dir}\n"
        
        return content_info.strip()
    except Exception as e:
        return f"Error: {e}"


#print(get_files_info("/home/norjoker/repos/AI_Agent/", "calculator"))