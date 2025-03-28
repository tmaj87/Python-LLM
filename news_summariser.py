import json
import os
from datetime import datetime

from bs4 import BeautifulSoup
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.documents import Document

from prompts import crypto_news_template, deepseek

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
)
search = DuckDuckGoSearchResults(backend="news", output_format="list", num_results=8)


def news_payload() -> str:
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
                "page_content": parsed.get_text(strip=True),
            }
        )
    return json.dumps(result, indent=2)


# sources:
# crypto-news-flash.com
# dailyhodl.com
# techstory.in
# ...


if __name__ == "__main__":
    news = deepseek.invoke(crypto_news_template(news_payload()))
    with open(
        "news/" + datetime.today().strftime("%Y-%m-%d_%H-%M-%S_news.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(news)
