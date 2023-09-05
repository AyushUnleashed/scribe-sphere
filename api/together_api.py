import requests
import os
from dotenv import load_dotenv

# Find the .env file in the current directory
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

# Load the environment variables from the .env file (if it exists)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

MODEL_NAME = "togethercomputer/llama-2-13b-chat"
base_model_name = MODEL_NAME.split("/")[-1]
MAX_TOKENS = 128

def start_instance() -> None:
    start_url = f"https://api.together.xyz/instances/start?model=togethercomputer%2F{base_model_name}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOGETHER_API_KEY}"
    }

    response = None
    try:
        response = requests.post(start_url, headers=headers)
    except Exception as e:
        print("Exception occurred with API", e)

    return response


def stop_instance() -> None:
    stop_url = f"https://api.together.xyz/instances/stop?model=togethercomputer%2F{base_model_name}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOGETHER_API_KEY}"
    }

    response = None
    try:
        response = requests.post(stop_url, headers=headers)
    except Exception as e:
        print("Exception occurred with API", e)

    return response


def fetch_llm_response(prompt: str):
    start_instance()
    inference_url = "https://api.together.xyz/inference"

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": MAX_TOKENS,
        "stop": ".",
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1
    }
    headers = {
        "authorization": f"Bearer {TOGETHER_API_KEY}",
        "accept": "application/json",
        "content-type": "application/json",
    }

    response = None
    try:
        response = requests.post(inference_url, json=payload, headers=headers)
    except Exception as e:
        print("Exception occurred with API", e)

    stop_instance()
    return response
