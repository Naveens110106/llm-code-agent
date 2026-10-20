import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import MultiLanguageSolution, build_coding_prompt

load_dotenv()

def generate_code_solutions (problem :str):
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
        structured_llm = llm.with_structured_output(MultiLanguageSolution)
        prompt = f"provide the solution for this question in python, java, and c++:{problem}"
        print(f"genrating solution for:'{problem}'...\n")
        result = structured_llm.invoke(prompt)
        return result.model_dump_json(indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)},indent =2)

if __name__ == "__main__":
    
    coading_problem = "Write an different function to find if a given string is a palindrome"
    json_output = generate_code_solutions(coading_problem)

print (json_output)


