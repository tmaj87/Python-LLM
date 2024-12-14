from typing import Dict


def get_llama3_2_config() -> Dict[str, str]:
    return {
        "model": "llama3.2:latest",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }


def get_qwen2_5_coder_config() -> Dict[str, str]:
    return {
        "model": "qwen2.5-coder:32b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }
