import os

from agents import get_supervisor, get_lead, get_dev, get_qa, get_sme
from const import (
    REPLAYS,
    INTERNAL_CONV_REPLAYS,
    SUMMARY_PROMPT,
    INTERNAL_CONV_SUMMARY,
)

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")


def reflection_message(recipient, _, sender):
    return f"""Review the following task solution idea. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"""


if __name__ == "__main__":
    lightweight_llm_config = {
        "model": OPENAI_MODEL,
        "api_key": AZURE_OPENAI_API_KEY,
        "base_url": OPENAI_BASE_URL,
        "api_version": OPENAI_API_VERSION,
        "api_type": "azure",
    }

    task = """
    We are ending year 2024 and there are no approaching contracts to fulfill in the next yet.
    We need to try to find a way to sustain our revenuer growth, an investment to put money into, a partner in US or UK to sign contract with.
    Put all your effort into it, as our and our families lives depend on it.
    Find that opportunity! 
    """

    supervisor = get_supervisor(lightweight_llm_config)
    lead = get_lead(lightweight_llm_config)
    sme = get_sme(lightweight_llm_config)
    dev = get_dev(lightweight_llm_config)
    qa = get_qa(lightweight_llm_config)

    # str or dict or None
    replay = supervisor.generate_reply(messages=[{"content": task, "role": "user"}])

    chat_queue = [
        {
            "recipient": qa,
            "message": reflection_message,
            "summary_method": "reflection_with_llm",
            "summary_args": {"summary_prompt": SUMMARY_PROMPT},
            "max_turns": INTERNAL_CONV_REPLAYS,
        },
        {
            "recipient": dev,
            "message": reflection_message,
            "summary_method": "reflection_with_llm",
            "summary_args": {"summary_prompt": SUMMARY_PROMPT},
            "max_turns": INTERNAL_CONV_REPLAYS,
        },
        {
            "recipient": sme,
            "message": reflection_message,
            "summary_method": "reflection_with_llm",
            "summary_args": {"summary_prompt": SUMMARY_PROMPT},
            "max_turns": INTERNAL_CONV_REPLAYS,
        },
        {
            "recipient": supervisor,
            "message": INTERNAL_CONV_SUMMARY,
            "max_turns": INTERNAL_CONV_REPLAYS,
        },
    ]

    lead.register_nested_chats(
        chat_queue=chat_queue,
        trigger=supervisor,
        # use_async
    )

    res = lead.initiate_chat(recipient=supervisor, message=task, max_turns=REPLAYS)

    print(res.summary)
