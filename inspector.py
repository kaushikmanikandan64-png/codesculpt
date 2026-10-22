import ast
from typing import List, Dict, Any

class CodeInspector(ast.NodeVisitor):
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.untyped_functions: List[Dict[str, Any]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # 1. Check for missing docstring
        has_docstring = ast.get_docstring(node) is not None
        
        # 2. Check for missing return type annotation
        has_return_type = node.returns is not None

        # 3. Check if args are missing type annotations
        untyped_args = [arg.arg for arg in node.args.args if arg.annotation is None]

        # Flag if docstring is missing OR any argument/return type lacks annotations
        if not has_docstring or not has_return_type or len(untyped_args) > 0:
            # Extract exact code slice of this function
            func_code = ast.get_source_segment(self.source_code, node)
            
            self.untyped_functions.append({
                "name": node.name,
                "line_no": node.lineno,
                "code": func_code,
                "missing_docstring": not has_docstring,
                "untyped_args": untyped_args,
                "missing_return_type": not has_return_type
            })

        # Continue traversing inner AST nodes
        self.generic_visit(node)

def inspect_file(file_path: str) -> tuple[str, List[Dict[str, Any]]]:
    """Reads a python file and returns its raw source + list of target functions."""
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    inspector = CodeInspector(source)
    inspector.visit(tree)
    
    return source, inspector.untyped_functions


if __name__ == "__main__":
    # Test on a dummy snippet
    sample = """
def calculate_area(length, width):
    return length * width
"""
    tree = ast.parse(sample)
    insp = CodeInspector(sample)
    insp.visit(tree)
    print("Detected target functions:", insp.untyped_functions)