import sys
import os
from inspector import inspect_file
from agent import refactor_function, validate_code_syntax

def run_codesculpt(target_file_path: str, output_file_path: str = None):
    if not os.path.exists(target_file_path):
        print(f"Error: File '{target_file_path}' not found.")
        return

    print(f"\n🔍 [1/3] Inspecting AST of '{target_file_path}'...")
    source_code, targets = inspect_file(target_file_path)

    if not targets:
        print("✅ No missing type hints or docstrings found! Your code looks great.")
        return

    print(f"💡 Found {len(targets)} function(s) needing refactoring:\n")
    for t in targets:
        print(f"   • Line {t['line_no']}: {t['name']}()")

    updated_code = source_code

    print("\n🤖 [2/3] Agentic Refactoring & Validation Loop...")
    for target in targets:
        original_snippet = target['code']
        print(f"\nProcessing '{target['name']}'...")
        
        # Agent action
        refactored_snippet = refactor_function(original_snippet)
        
        # Safety validation step
        is_valid = validate_code_syntax(refactored_snippet)
        
        if is_valid:
            print(f"  ✓ Syntax check passed for '{target['name']}'. Replacing snippet...")
            updated_code = updated_code.replace(original_snippet, refactored_snippet)
        else:
            print(f"  ✗ Syntax check failed for '{target['name']}'. Keeping original code.")

    # Save output
    out_path = output_file_path or f"refactored_{os.path.basename(target_file_path)}"
    print(f"\n💾 [3/3] Writing updated code to '{out_path}'...")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(updated_code)

    print("\n✨ Done! Refactoring complete.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_python_file.py>")
    else:
        run_codesculpt(sys.argv[1])