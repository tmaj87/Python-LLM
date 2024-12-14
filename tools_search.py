import json
import os

from bs4 import BeautifulSoup
from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM

from prompts import llm

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
)
search = DuckDuckGoSearchResults(backend="news", output_format="list", num_results=2)


def v1() -> str:
    links: list[str] = []
    result: list[dict[str, str]] = []
    for obj in search.invoke("crypto finance today"):
        links.append(obj.get("link", ""))
    loader = AsyncHtmlLoader(links)
    load: list[Document] = loader.load()
    for doc in load:
        parsed = BeautifulSoup(doc.page_content or "", "html.parser")
        result.append(
            {
                "source": doc.metadata.get("source", ""),
                "title": doc.metadata.get("title", ""),
                "language": doc.metadata.get("language", ""),
                "page_content": parsed.get_text(strip=True),
            }
        )
    return json.dumps(result)


def v2() -> AgentExecutor:
    llm = OllamaLLM(model="llama3.2")
    async_browser = create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    tools = toolkit.get_tools()
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.SELF_ASK_WITH_SEARCH,
        verbose=True,
    )


if __name__ == "__main__":
    res = v1()
    # res = v2().arun("Get latest crypto news")
    print(
        llm.invoke(
            f"""
You are able to understand JSON formatting.
Here is a list of json objects holding latest news:

{res}

Create list of latest news.
One news record per unique source.
Try to assume date from provided source url or news content.
Notes contains (if mentioned about):
- names of cryptocurrencies
- names of stork market assets
- names of financial institutions
- name of new financial laws
Title is a 6 words page_content summary.
Body is a 4 sentence page_content summary.

Every news block should look as follows:

## [title]

[body]

- Date: [date]
- Source: [url]
- Notes: [notes]
"""
        )
    )
