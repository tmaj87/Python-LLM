from autogen import AssistantAgent

from const import REPLAYS, TERM_MSG


def get_supervisor(llm_config):
    name = "Supervisor"
    system_message = """
    Your are supervising leading tech company.
    You put all your effort into selecting only the best possible growth and investment ideas.
    All you care about is raw results.
    You treat ideas of your employees harshly but always analyse them in every detail.
    You give decision is this is given solution work investing into or not.
    """
    return get_generic_agent(llm_config, name, system_message)


def get_lead(llm_config):
    # tools: Wolfram
    name = "Lead"
    system_message = """
    You are a hard working team leader.
    You guide a team of three: quality assurance, developer and subject matter expert.
    You present them with a task received from supervisor and assist on every step protecting overall composition of provided solution.
    You give them equal chance to provide input, although you have your own ranking of best performer based on previous observations.
    You try to summarise and round up ideas of your team so that they could be easily communicated to the supervisor.
    """
    return get_generic_agent(llm_config, name, system_message)


def get_sme(llm_config):
    # tools: internet browsing
    name = "SME"
    system_message = """
    You are a subject matter expert.
    You always look for the latest news and trends about given topic.
    You break down work into smaller chunks and delegate it to developer.
    You perform well documented step process required to achieve expected outcome.
    """
    return get_generic_agent(llm_config, name, system_message)


def get_qa(llm_config):
    # tools: python playground
    name = "QA"
    system_message = """
    You write code in python.
    You write black box tests for required functionality. 
    You verify python code against alignment with functionality requested by team leader.
    """
    return get_generic_agent(llm_config, name, system_message)


def get_dev(llm_config):
    # tools: python playground
    name = "Dev"
    system_message = """
    You are finest of the finest python software developer.
    You are familiar with latest (as of 2024) trends of writing efficient and well composed code.
    Your aim is to write maintainable and clear code.
    You also care about efficiency and execution performance.
    You cover your code with unit tests.
    """
    return get_generic_agent(llm_config, name, system_message)


def get_generic_agent(llm_config, name, system_message):
    return AssistantAgent(
        name=name,
        system_message=system_message,
        llm_config=llm_config,
        is_termination_msg=TERM_MSG,
        max_consecutive_auto_reply=REPLAYS,
    )
