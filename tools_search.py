import os

from bs4 import BeautifulSoup
from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
)
search = DuckDuckGoSearchResults(backend="news", output_format="list", num_results=3)


def v1() -> list[Document]:
    links: list[str] = []
    result: list[Document] = []
    for obj in search.invoke("crypto finance"):
        links.append(obj.get("link", ""))
    loader = AsyncHtmlLoader(links)
    load: list[Document] = loader.load()
    for doc in load:
        # remove js and html
        soup = BeautifulSoup(doc.page_content or "", "html.parser")
        doc.page_content = soup.get_text(strip=True)
        result.append(doc)
    return result


def v2() -> AgentExecutor:
    llm = OllamaLLM(model="llama3.2")
    async_browser = create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    tools = toolkit.get_tools()
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )


if __name__ == "__main__":
    res = v1()
    # res = v2().arun("Get me latest crypto news")
    print(res)
