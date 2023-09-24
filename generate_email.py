from typing import Dict
from data_source.company_info import fetch_company_info
from data_source.user_info import fetch_user_info
from api.together_api import fetch_llm_response
from api.gpt_for_everyone import fetch_gpt_response
from api.gpt_api import fetch_openai_response
from api.prompts import BASE_PROMPT


def prepare_llm_prompt_2(user_info: Dict, company_info: Dict) -> str:
    # Prepare the prompt for LLM.
    llm_prompt = BASE_PROMPT
    llm_prompt += f"\n ---"
    llm_prompt += f"\nUser's Details:\n{user_info}"
    llm_prompt += f"\n ---"
    llm_prompt += f"\nCompany's Details:\n{company_info}"
    llm_prompt += f"\n ---"
    return llm_prompt


def prepare_llm_prompt(user_info: Dict, company_info: Dict) -> str:
    # Prepare the prompt for LLM.
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


def generate_email(company_info="") -> str:
    # Fetch student and company info

    user_info: Dict = fetch_user_info()
    if company_info == "":
        company_info: Dict = fetch_company_info()

    # Prepare llm prompt
    # llm_prompt: str = prepare_llm_prompt(user_info, company_info)
    llm_prompt_2: str = prepare_llm_prompt_2(user_info, company_info)

    # message = get_together_api_message(llm_prompt)
    message = get_gpt_for_everyone_message(llm_prompt_2)
    # message = fetch_openai_response(llm_prompt)
    return message


if __name__ == "__main__":
    generate_email()
