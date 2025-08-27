# Python-LLM Multi-Agent System

A comprehensive Python 3.12 codebase featuring multiple AI agents and LLM-powered tools for various applications.

## 🚀 Features

- **Multi-Agent Conversations**: AutoGen-based agent interactions
- **Reflection Agents**: LangGraph-powered self-improving agents
- **Search Agents**: Web scraping and search capabilities
- **News Summarization**: Automated crypto news analysis
- **Expert Interview System**: AI-powered technical interview tools
- **Embedding Systems**: ChromaDB-based document retrieval
- **Template Chains**: Reusable LLM prompt templates

## 📁 Project Structure

```
Python-LLM/
├── agents.py                 # AutoGen agent definitions
├── multi_agents_talk.py      # Multi-agent conversation system
├── reflect_agent.py          # LangGraph reflection agent
├── search_agent.py           # Web search and browser automation
├── news_summariser.py        # Crypto news scraping and analysis
├── embedding.py              # ChromaDB embedding system
├── template_chain.py         # LLM template chains
├── prompts.py                # LangChain prompt templates
├── utils.py                  # Configuration utilities
├── const.py                  # Constants and settings
├── expert_interview/         # Expert interview module
│   ├── interviewer.py        # Main interviewer class
│   ├── templates.py          # Interview templates
│   ├── qa_guide.md          # Q&A interview guide
│   └── README.md            # Module documentation
├── news/                     # Generated news files
├── docs/                     # Documentation
└── requirements.txt          # Python dependencies
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Python-LLM
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Ollama** (for local LLM models)
   ```bash
   # Install Ollama and download models
   ollama pull qwen2.5-coder:32b
   ollama pull llama3.2
   ```

## 🎯 Quick Start

### Expert Interview System
```python
from expert_interview import ExpertInterviewer

interviewer = ExpertInterviewer()
questions = interviewer.generate_questions()
print(questions)
```

### Multi-Agent Conversations
```python
from multi_agents_talk import process

result = process("Your task description here")
print(result)
```

### News Summarization
```python
from news_summariser import news_payload

news_data = news_payload()
print(news_data)
```

## 🔧 Configuration

- **API Keys**: Set your own API keys for external services
- **Ollama Models**: Configure local LLM models in `utils.py`
- **Agent Settings**: Customize agent behaviors in `const.py`

## 📚 Documentation

- **Expert Interview Module**: See `expert_interview/README.md`
- **Agent System**: Check `agents.py` and `multi_agents_talk.py`
- **Template System**: Review `template_chain.py` and `prompts.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.