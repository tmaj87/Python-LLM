"""
Expert Interview Module

This module contains comprehensive interview guides and templates for technical interviews.
It provides both question templates and detailed answer examples for various roles.
"""

from .interviewer import ExpertInterviewer
from .templates import company_template, another_company_template

__version__ = "1.0.0"
__author__ = "Python-LLM Team"

__all__ = [
    "ExpertInterviewer",
    "company_template", 
    "another_company_template"
] 