from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM

llama_3_2 = OllamaLLM(model="llama3.2")
qwen_2_5_instruct = OllamaLLM(model="qwen2.5:32b-instruct")
qwq = OllamaLLM(model="qwq:32b")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an essay assistant tasked with writing excellent 5-paragraph essays."
            "Generate the best essay imaginable for the user's request."
            "If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
generate = prompt | qwen_2_5_instruct

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a teacher grading an essay submission."
            "Generate critique and recommendations for the user's submission."
            "Provide detailed recommendations, including requests for length, depth, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
reflect = reflection_prompt | qwen_2_5_instruct


def crypto_news_template(news_payload: str):
    return f"""
    Here is a list of JSON objects holding latest news:

    {news_payload}

    Whenever some updates are required, please use latest version.
    Every news block should look as follows:

    ## title (from object)

    6 sentence page_content (from object) summary

    - Date - asses date from provided news content
    - Source - source (from object; as url)
    - Highlights - contains sections about:
        - cryptocurrencies (When section is present, provide exact names involved. Hide section when there's no relevant information.)
        - stork market (When section is present, provide exact names involved. Hide section when there's no relevant information.)
        - financial institutions (When section is present, provide exact names involved. Hide section when there's no relevant information.)
        - financial regulations (When section is present, provide exact names involved. Hide section when there's no relevant information.)
    """
