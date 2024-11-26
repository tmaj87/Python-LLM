import os

from agents import get_supervisor, get_lead, get_dev, get_qa, get_sme
from const import (
    REPLAYS,
    INTERNAL_CONV_REPLAYS,
    SUMMARY_PROMPT,
    INTERNAL_CONV_SUMMARY,
)


def reflection_message(recipient, _, sender) -> str:
    return f"""Review the following task solution idea. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"""


if __name__ == "__main__":
    config = {
        "model": os.getenv("OPENAI_MODEL"),
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "base_url": os.getenv("OPENAI_BASE_URL"),
        "api_version": os.getenv("OPENAI_API_VERSION"),
        "api_type": "azure",
    }
    supervisor = get_supervisor(config)
    lead = get_lead(config)
    sme = get_sme(config)
    dev = get_dev(config)
    qa = get_qa(config)
    task = """
    We are ending year 2024 and there are no approaching contracts to fulfill in the next yet.
    We need to try to find a way to sustain our revenuer growth, an investment to put money into, a partner in US or UK to sign contract with.
    Put all your effort into it, as our and our families lives depend on it.
    Find that opportunity! 
    """
    replay = supervisor.generate_reply(messages=[{"content": task, "role": "user"}])
    chat_queue = [
        {
            "recipient": sme,
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
            "recipient": qa,
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
