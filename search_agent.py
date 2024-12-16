from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain_ollama import OllamaLLM


def get_agent() -> AgentExecutor:
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
    res = get_agent().run("Get latest crypto news")
    print(res)
