# CodeSculpt 🛠️🤖

A local developer tool and agentic workflow that automatically detects missing Python type hints and docstrings, refactors them using Gemini, and validates the output using Python's native AST parser before modifying code.

---

## 🚀 How It Works
1. **Inspects:** Parses target Python files using Python's built-in `ast` module to locate functions lacking type annotations or docstrings.
2. **Refactors:** Passes untyped function snippets to Gemini with strict formatting instructions to inject type hints and Google-style docstrings.
3. **Validates (Safety Guardrail):** Runs `ast.parse()` on the generated code to programmatically ensure zero syntax errors exist before saving changes.

---

## 📂 Project Structure
```text
codesculpt/
├── inspector.py        # AST static analysis and code smell detection
├── agent.py            # Gemini client integration and syntax safety checks
├── main.py             # CLI orchestrator and file writer
├── test_script.py      # Sample script for testing
└── .env                # Environment variables (API Key


python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

##Install Dependencies
pip install google-genai python-dotenv

Set up your API Key:
Create a .env file in the root directory and add your Google Gemini API key:
API_KEY=your_api_key_here
