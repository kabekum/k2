"""
LLM-agnostic summarizer
(OpenAI, Azure, local LLM can be plugged in)
"""

def summarize_text(text: str) -> str:
    sentences = text.split('.')[:5]
    return '.'.join(sentences) + '.'
