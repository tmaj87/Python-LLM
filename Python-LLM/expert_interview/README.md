# Expert Interview Module

This module provides comprehensive tools for conducting technical interviews using AI-powered question generation and response evaluation.

## Structure

```
expert_interview/
├── __init__.py              # Module initialization and exports
├── interviewer.py           # Main interviewer class and functionality
├── templates.py             # Interview prompt templates
├── qa_guide.md             # Q&A format interview guide
├── answers_guide.md        # Detailed answers for standard questions
├── advanced_answers.md     # Advanced interview questions and answers
└── README.md               # This file
```

## Features

- **ExpertInterviewer Class**: Main class for generating interview questions
- **Multiple Templates**: Support for different interview types and company requirements
- **Comprehensive Guides**: Pre-written Q&A guides for various technical roles
- **LangChain Integration**: Uses LangChain and Ollama for AI-powered question generation

## Usage

### Basic Usage

```python
from expert_interview import ExpertInterviewer

# Create an interviewer
interviewer = ExpertInterviewer()

# Generate questions using default template
questions = interviewer.generate_questions()

# Generate advanced questions
advanced_questions = interviewer.generate_questions_advanced()
```

### Using Templates

```python
from expert_interview import company_template, another_company_template

# Use specific templates
questions = interviewer.generate_questions(company_template)
advanced = interviewer.generate_questions(another_company_template)
```

### Convenience Functions

```python
from expert_interview import get_company_interviewer, get_advanced_interviewer

# Get pre-configured interviewers
company_interviewer = get_company_interviewer()
advanced_interviewer = get_advanced_interviewer()
```

## Templates

### Company Template
Standard template for Python Software Engineer positions with focus on:
- Python development experience
- ML frameworks (Keras, TensorFlow, Jupyter)
- AWS cloud services
- API development
- Database technologies
- Logging and troubleshooting

### Advanced Company Template
Comprehensive template for senior positions covering:
- Modern Python frameworks
- LLM-based solutions
- RAG and search pipelines
- Cloud platforms and containerization
- ML Ops and workflow orchestration
- Security and compliance

## Documentation Files

- **qa_guide.md**: Complete Q&A format with 21 questions and concise answers
- **answers_guide.md**: Detailed responses for standard technical interview questions
- **advanced_answers.md**: Advanced questions covering modern AI/ML development practices

## Requirements

- Python 3.12+
- langchain-core
- langchain-ollama
- ollama (with qwen2.5-coder:32b model)

## Installation

The module is part of the main Python-LLM project. Install dependencies:

```bash
pip install -r requirements.txt
```

## Example

```python
from expert_interview import ExpertInterviewer

interviewer = ExpertInterviewer("qwen2.5-coder:32b")
questions = interviewer.generate_questions()

print("Generated Interview Questions:")
print(questions)
``` 