import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser()
parser.add_argument("prompt",  help="input for LLM to process")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


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
    contents=messages
    )

    print(response.text)

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
