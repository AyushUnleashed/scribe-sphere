from typing import Dict
from data_source.company_info import fetch_company_info
from data_source.user_info import fetch_user_info
from api.together_api import fetch_llm_response
from api.gpt_for_everyone import fetch_gpt_response

BASE_PROMPT = """You are GPT, an AI with vast knowledge in the field of job applications. You need to write a 
personalized cold email for the user who is looking for an SDE intern/full-time opportunity based on the company's 
details provided. The email should be professional and show the user's interest in the company. if nothing is given 
about receiver use "Hello Team {company_time} for starting Do not generate fake details. Use only the information 
given Start with SUBJECT: Then in the next line write the complete content, starting with CONTENT: The email needs to 
end with the user looking forward to hearing back from the company. It should be crisp & to the point; founders don't 
have much time.Use relevant details from User's experience & skills to write directed email If you add any fields as 
variables use only this format eg: {variable1_name} & list them at the end line. eg: VARIABLES: ["variable1_name"] 
All variables are , separated ,snake_case named, if no need for any variables, give VARIABLES: [None] """


def prepare_llm_prompt(user_info: Dict, company_info: Dict) -> str:
    # Prepare the prompt for LLM.
    llm_prompt = BASE_PROMPT
    llm_prompt += f"\n ---"
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
        response_json = gpt_response_text.json()
        message = response_json['output']['choices'][0]['text']
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
    llm_prompt: str = prepare_llm_prompt(user_info, company_info)

    # message = get_together_api_message(llm_prompt)
    message = get_gpt_for_everyone_message(llm_prompt)
    return message


if __name__ == "__main__":
    generate_email()
