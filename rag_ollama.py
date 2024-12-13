from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="qwen2.5-coder:32b")
template = """Question: {question}

Answer: Let's think step by step."""

if __name__ == "__main__":
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    res = chain.invoke({"question": "Create a single page application."})
    print(res)
