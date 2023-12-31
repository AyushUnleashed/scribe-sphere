from typing import Dict
from data_source.company_info import fetch_company_info
from fetch_user_info_email import fetch_user_info_from_email
from api.together_api import fetch_llm_response
from api.gpt_for_everyone import fetch_gpt_response
from api.gpt_api import fetch_openai_response, set_system_prompt
from api.prompts import BASE_PROMPT
import os


def prepare_llm_prompt_2(user_info: Dict, company_info) -> str:
    # Prepare the prompt for LLM.
    llm_prompt = BASE_PROMPT
    llm_prompt += f"\n ---"
    llm_prompt += f"\nUser's Details:\n{user_info}"
    llm_prompt += f"\n ---"
    llm_prompt += f"\nCompany's Details:\n{company_info}"
    llm_prompt += f"\n ---"
    return llm_prompt


def prepare_llm_prompt(user_info: Dict, company_info) -> str:
    # Prepare the prompt for LLM.
    set_system_prompt(BASE_PROMPT)
    llm_prompt = f"\n ---"
    llm_prompt += f"\nUser's Details:\n{user_info}"
    llm_prompt += f"\n ---"
    llm_prompt += f"\nCompany's Details:\n{company_info}"
    llm_prompt += f"\n ---"
    return llm_prompt


def get_together_api_message(llm_prompt):
    # Fetch llm response
    llm_response = fetch_llm_response(llm_prompt)

    if llm_response:
        response_json = llm_response.json()
        message = response_json['output']['choices'][0]['text']
        # message = gpt_response_text
        print(f"\nHere is the personalized cold email for SDE intern/full time opportunity:\n{message}")
        return message
    else:
        print("Failed to generate the email.")
        return ""


def get_gpt_for_everyone_message(llm_prompt):
    # Fetch llm response

    gpt_response_text = fetch_gpt_response(llm_prompt)

    if gpt_response_text:

        message = gpt_response_text
        # message = gpt_response_text
        print(f"\nHere is the personalized cold email for SDE intern/full time opportunity:\n{message}")
        return message
    else:
        print("Failed to generate the email.")
        return ""


def generate_email(email, company_info="", company_name="") -> str:
    # Fetch student and company info
    use_metaphor = True

    # user_info: Dict = fetch_user_info()
    user_info = fetch_user_info_from_email(email)
    if company_info == "" and company_name != "":

        if use_metaphor:
            from get_company_description import get_company_info_from_name
            company_info = get_company_info_from_name(company_name)

        else:
            # company_info: Dict = fetch_company_info()
            from get_company_website import get_website_by_company_name
            website_url = get_website_by_company_name(company_name)
            from get_company_description import get_company_info_from_url
            company_info = get_company_info_from_url(website_url)

    if company_info:
        # Prepare llm prompt
        pre_str = f"company name: {company_name} \n "
        llm_prompt: str = prepare_llm_prompt(user_info, company_info)
        # llm_prompt_2: str = prepare_llm_prompt_2(user_info, pre_str + company_info)

        # message = get_together_api_message(llm_prompt)
        # message = get_gpt_for_everyone_message(llm_prompt_2)
        message = fetch_openai_response(llm_prompt)
        save_message_to_file(message)

        return message
    else:
        return "Something went wrong "


def save_message_to_file(message, folder_name="generations", file_name="generated_email.txt"):
    # Check if the folder exists, and if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Define the file path
    file_path = os.path.join(folder_name, file_name)

    # Save the message to the file
    with open(file_path, "w") as file:
        file.write(message)

    print(f"Message saved to {file_path}")


if __name__ == "__main__":
    message = generate_email()
