"""
Expert Interviewer

This module provides the main interviewer functionality using LangChain and Ollama.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from .templates import company_template, another_company_template


class ExpertInterviewer:
    """
    Expert Interviewer class for conducting technical interviews.
    
    This class provides functionality to generate interview questions and responses
    using different templates and LLM models.
    """
    
    def __init__(self, model_name: str = "qwen2.5-coder:32b"):
        """
        Initialize the ExpertInterviewer.
        
        Args:
            model_name: The Ollama model to use for generating questions
        """
        self.model = OllamaLLM(model=model_name)
        self.chain = None
    
    def create_chain(self, template: str) -> ChatPromptTemplate:
        """
        Create a LangChain prompt template from the given template.
        
        Args:
            template: The prompt template string
            
        Returns:
            ChatPromptTemplate: The compiled chain
        """
        prompt = ChatPromptTemplate.from_template(template)
        self.chain = prompt | self.model
        return self.chain
    
    def generate_questions(self, template: str = None) -> str:
        """
        Generate interview questions using the specified template.
        
        Args:
            template: The template to use (defaults to company_template)
            
        Returns:
            str: Generated interview questions
        """
        if template is None:
            template = company_template
            
        chain = self.create_chain(template)
        return chain.invoke({"request": "Generate interview questions"})
    
    def generate_questions_advanced(self) -> str:
        """
        Generate advanced interview questions using the another_company_template.
        
        Returns:
            str: Generated advanced interview questions
        """
        return self.generate_questions(another_company_template)


# Convenience functions for backward compatibility
def get_company_interviewer() -> ExpertInterviewer:
    """Get an interviewer configured for company interviews."""
    return ExpertInterviewer()


def get_advanced_interviewer() -> ExpertInterviewer:
    """Get an interviewer configured for advanced interviews."""
    return ExpertInterviewer()


if __name__ == "__main__":
    # Example usage
    interviewer = ExpertInterviewer()
    questions = interviewer.generate_questions()
    print("Generated Questions:")
    print(questions)
