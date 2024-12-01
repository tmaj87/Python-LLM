from agents import get_owner, get_lead, get_dev, get_qa, get_sme
from const import (
    REPLAYS,
    INTERNAL_CONV_REPLAYS,
    SUMMARY_PROMPT,
    INTERNAL_CONV_SUMMARY,
)
from utils import get_config


def reflection_message(recipient, _, sender) -> str:
    return f"""Review the following task solution idea. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"""


def process(task: str):
    config = get_config()
    owner = get_owner(config)
    lead = get_lead(config)
    sme = get_sme(config)
    dev = get_dev(config)
    qa = get_qa(config)
    replay = owner.generate_reply(messages=[{"content": task, "role": "user"}])
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
            "recipient": lead,
            "message": INTERNAL_CONV_SUMMARY,
            "max_turns": INTERNAL_CONV_REPLAYS,
        },
    ]
    lead.register_nested_chats(
        chat_queue=chat_queue,
        trigger=owner,
        # use_async
    )
    return lead.initiate_chat(recipient=owner, message=task, max_turns=REPLAYS)


if __name__ == "__main__":
    result = process(
        """
    We are ending year 2024 and there are no approaching contracts to fulfill in the next yet.
    We need to try to find a way to sustain our revenuer growth, an investment to put money into, a partner in US or UK to sign contract with.
    Put all your effort into it, as our and our families lives depend on it.
    Find that opportunity! 
    """
    )
    print(result.summary)
