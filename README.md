# CodeSculpt 🛠️🤖

> *An AST-Powered Autonomous Python Refactoring Agent with Deterministic Safety Guardrails*

**CodeSculpt** is a local developer-tool agent designed to inspect Python source code, identify code smells (missing type hints and documentation), use an LLM to generate clean refactoring improvements, and validate the output through programmatic safety guardrails before modifying codebases.

---

## 📌 Repository Description

An AST-powered autonomous Python refactoring agent that uses static code analysis, LLM generation, and safety validation loops to add type hints and docstrings.

---

## ✨ Key Features

* **Deterministic Static Analysis:** Uses Python's native `ast` (Abstract Syntax Tree) library to precisely locate function definitions lacking type hints or docstrings, avoiding arbitrary text searching.
* **Controlled Agentic Loop:** Implements a closed-loop perception-action-validation cycle:
  1. **Perception:** Inspects AST nodes and extracts untyped code snippets.
  2. **Action:** Prompts Gemini to inject Google-style docstrings and type annotations.
  3. **Validation:** Executes a programmatic syntax check (`ast.parse()`) to verify code integrity prior to replacement.
* **Zero-Cloud Infrastructure:** Runs locally as a lightweight command-line tool, making it fast, secure, and easy to audit.

---

## 🏗️ Architecture & Workflow

```text
[Target Python File] ➔ [AST Inspector (inspector.py)] ➔ [Extract Untyped Functions]
                                                                │
[Write Updated Code] ◄─ [AST Syntax Guardrail (agent.py)] ◄─ [Gemini Refactoring Agent]
```

---

## 📂 Project Structure

```text
codesculpt/
│
├── inspector.py        # AST static analysis and code smell detection
├── agent.py            # Gemini client integration and syntax safety checks
├── main.py             # CLI orchestrator and file writer
├── test_script.py      # Sample messy script for testing
├── .env                # Local environment variables (API Key)
└── README.md           # Project documentation
```

---

## 📋 Requirements & Prerequisites

* **Python:** 3.10 or higher
* **API Key:** Google Gemini API Key (Get a free key at [Google AI Studio](https://ai.google.dev/))

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/codesculpt.git
   cd codesculpt
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   ```
   * **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   * **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install google-genai python-dotenv
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root directory and add your key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

---

## 💻 Usage

Run CodeSculpt on any target Python file using the CLI runner:

```bash
python main.py test_script.py
```

### **Sample Execution Flow:**
1. The inspector analyzes `test_script.py` and locates missing docstrings or type hints.
2. The agent sends the raw code snippets to Gemini to generate updated snippets.
3. Each snippet undergoes an `ast.parse()` syntax check.
4. If valid, the updated functions are saved to `refactored_test_script.py`.

---

## 🎓 Engineering Takeaways

* **Guardrails over Blind Trust:** Allowing an LLM to freely modify source code is risky. CodeSculpt introduces a hard programmatic validation check (`ast.parse()`) acting as a gatekeeper—if the generated code introduces a syntax error, the agent rejects it and preserves the original code.
* **Bridging Deterministic and Probabilistic Systems:** Combining Python's strict AST parsing with flexible LLM prompt generation demonstrates how software engineering fundamentals can safely harness generative AI.
