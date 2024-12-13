from typing import Dict


def get_config() -> Dict[str, str]:
    return {
        "model": "llama3.2:latest",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }
