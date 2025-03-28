from typing import Dict


def get_llama3_2_config() -> Dict[str, str]:
    return {
        "model": "llama3.2:latest",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }


def get_deepseek_config() -> Dict[str, str]:
    return {
        "model": "deepseek-r1:32b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }


def get_speakleash_config() -> Dict[str, str]:
    return {
        "model": "SpeakLeash/bielik-11b-v2.3-instruct:Q8_0",
        "base_url": "http://localhost:11434/v1",
        "api_key": "api_key",
    }
