import os
import ast
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(dotenv_path= "Credidentials.env")

APIKEY = os.getenv("API_KEY")

def refactor_function(func_code: str) -> str:
    """Uses Gemini to add type hints and docstrings to a function snippet."""
    client = genai.Client(api_key=APIKEY)

    prompt = f"""You are a strict Python software engineer. 
Refactor the following Python function by:
1. Adding proper type hints to all arguments and the return type.
2. Adding a clear Google-style docstring explaining args and return values.
3. Preserving the exact internal logic of the function.

Return ONLY valid raw Python code for the refactored function. Do NOT include markdown code blocks (like ```python ... ```) or conversational commentary.

Function snippet to improve:
{func_code}
"""

    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.1  # Low temperature for deterministic code output
        )
    )

    clean_code = response.text.strip()
    
    # Clean up markdown formatting if present
    if clean_code.startswith("```python"):
        clean_code = clean_code[9:]
    if clean_code.startswith("```"):
        clean_code = clean_code[3:]
    if clean_code.endswith("```"):
        clean_code = clean_code[:-3]
        
    return clean_code.strip()


def validate_code_syntax(code_snippet: str) -> bool:
    """Safety Guardrail: Ensures generated code is valid, parseable Python."""
    try:
        ast.parse(code_snippet)
        return True
    except SyntaxError as e:
        print(f"[SAFETY ALERT] Generated code has syntax error: {e}")
        return False