import os
from typing import Dict


def get_config() -> Dict[str, str]:
    return {
        "model": os.getenv("OPENAI_MODEL"),
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "base_url": os.getenv("OPENAI_BASE_URL"),
        "api_version": os.getenv("OPENAI_API_VERSION"),
        "api_type": "azure",
    }
