from autogen import ChatResult, GroupChat, GroupChatManager

from agents import get_owner, get_lead, get_sme, get_dev, get_qa
from utils import get_llama3_2_config


def reflection_message(recipient, messages, sender, config) -> str:
    return f"""Review the following task solution idea. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"""


def lead_message(recipient, messages, sender, config) -> str:
    return f"""
    This is a task from your supervisor.
    Threat it with maximum attention and focus on details.
    
    The task:
    {messages[0].get("content", "")}
    
    Break down Supervisor instructions into actionable items that can be solved by your team members.
    Your team consist of 3 personas:
    - sme, subject matter expert
    - dev, software developer specialised in python
    - qa, quality assurance
    Create a separate message for every team member with pointed list of tasks to perform.
    """


def process(task: str) -> ChatResult:
    config = get_llama3_2_config()
    owner = get_owner(config)
    lead = get_lead(config)
    chat_manager = get_lead(config)
    sme = get_sme(config)
    dev = get_dev(config)
    qa = get_qa(config)

    group_chat = GroupChat(
        agents=[lead, qa, dev, sme],
        messages=[],
        # max_round=6,
        speaker_selection_method="round_robin",
    )

    group_chat_manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=chat_manager.llm_config,
    )

    return owner.initiate_chat(
        group_chat_manager,
        message=task,
        summary_method="reflection_with_llm",
    )


if __name__ == "__main__":
    result = process(
        """
    We are ending year 2024 and there are no approaching contracts to fulfill in the next yet.
    We need to try to find a way to sustain our revenuer growth, an investment to put money into, a partner in US or UK to sign contract with.
    Put all your effort into it, as our and our families lives depend on it.
    Find that opportunity! 
    """
    )
    print(result)
