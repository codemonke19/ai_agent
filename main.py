import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
    for _ in range(MAX_ITERS):
        try:
            last_content = generate_content(client, messages, args.verbose)
            if last_content:
                print("Final Response:")
                print(last_content)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")
    print(f"Maximum iterations ({MAX_ITERS}) reached without the model returning a final response")
    sys.exit(1)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = messages,
        config = types.GenerateContentConfig(
            tools = [available_functions], system_instruction=system_prompt
        ),
    )
    if not response.usage_metadata:
        raise RuntimeError("Error: failed API request!")
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if not response.function_calls and response.text: 
        return response.text
    
    for item in response.candidates:
        messages.append(item.content)

    function_results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose=verbose)
        if not function_call_result.parts:
            raise Exception("Function call returned no parts")
        if not function_call_result.parts[0].function_response:
            raise Exception("Function call returned no function_response")
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function call returned no response data")
        function_results.append(function_call_result.parts[0])
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
    
    messages.append(types.Content(role="user", parts=function_results))


if __name__ == "__main__":
    main()
