import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse
from config import SYSTEM_PROMT, WORKING_DIRECTORY
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser()
parser.add_argument("prompt",  help="input for LLM to process")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    if function_call_part.name == "get_files_info":
        function_result = get_files_info(WORKING_DIRECTORY,**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    elif function_call_part.name == "run_python_file":
        function_result = run_python_file(WORKING_DIRECTORY,**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    elif function_call_part.name == "write_file":
        function_result = write_file(WORKING_DIRECTORY,**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    elif function_call_part.name == "get_file_content":
        function_result = get_file_content(WORKING_DIRECTORY,**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )




def main():
    if len(sys.argv) <= 1:
        print("Error: no prompt found")
        sys.exit(1)
    
    user_prompt = args.prompt

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions],
                                       system_instruction=SYSTEM_PROMT)
    )

    function_call_parts = response.function_calls
    for fn in function_call_parts:
        #print(f"Calling function: {fn.name}({fn.args})")
        if args.verbose:
            function_call_result = call_function(fn, verbose=True)
        else:
            function_call_result = call_function(fn)
        print(f"-> {function_call_result.parts[0].function_response.response}")


    print(response.text)

    #if args.verbose:
        #print(f"User prompt: {user_prompt}")
        #print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        #print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
