from typing import Dict


def fetch_company_info() -> Dict:
    # Get the company's name and description
    info = {
        "company_name": "Hexo.ai",
        "company_description": "Maximize Marketing ROI with Generative AI, Personalize your marketing communication. "
                               "At scale.. "
    }

    info_2 = {
        "to": "Rohit Agarwal",
        "designation": "Co-Founder",
        "company_name": "portkey.ai",
        "company_description": """ Portkey enables companies to develop, launch, maintain & iterate over their generative AI apps and features faster. Companies can add observability, model management, experimentation and compliance to their products through an integration which takes less than a minute. """
    }

    info_3 = {
        "company_name": "jar app",
        "company_description": "Jar, a platform used to encourage savings habits in Indians by helping them save on a daily basis. "
    }
    return info_3
