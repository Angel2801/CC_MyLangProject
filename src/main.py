# src/main.py

from src.lexer.lexer import lexer
from src.parser.parser import parser
from src.semantic_analysis import SemanticAnalyzer
from src.compiler.code_generator import CodeGenerator

def main():
    # Sample input code with multiple statements
    code = """
    let x = 5 + 3
    x * 2
    """

    # Split the code into individual lines (statements)
    statements = code.strip().splitlines()

    # Initialize the semantic analyzer and code generator
    analyzer = SemanticAnalyzer()
    generator = CodeGenerator()

    for line in statements:
        # Step 1: Lexical Analysis
        print("Lexical Analysis:")
        lexer.input(line)
        for token in lexer:
            print(token)
        print("\n")

        # Step 2: Parsing
        print("Parsing to generate AST:")
        ast = parser.parse(line)
        print("AST:", ast)
        print("\n")

        # Step 3: Semantic Analysis
        print("Semantic Analysis:")
        try:
            analyzer.analyze(ast)
            print("Semantic Analysis passed!\n")
        except NameError as e:
            print(f"Semantic Analysis error: {e}")
            return

        # Step 4: Code Generation and Execution
        print("Code Generation and Execution:")
        result = generator.generate(ast)
        print("Result:", result)
        print("\n")

if __name__ == "__main__":
    main()
