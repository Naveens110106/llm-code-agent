# tools.py
from pydantic import BaseModel, Field

class MultiLanguageSolution(BaseModel):
    question: str = Field(description="The original coding question asked by the user")
    python_solution: str = Field(description="Complete solution written in Python")
    javascript_solution: str = Field(description="Complete solution written in JavaScript")
    java_solution: str = Field(description="Complete solution written in Java")
    cpp_solution: str = Field(description="Complete solution written in C++")
    explanation: str = Field(description="Brief explanation of the algorithm")

def build_coding_prompt(question: str) -> str:
    return f"Provide clean, working code solutions for the following problem in Python, JavaScript, Java, and C++: {question}"