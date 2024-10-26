# tests/test_code_generator.py
from src.parser.parser import parser
from src.compiler.code_generator import CodeGenerator

def test_code_generator():
    generator = CodeGenerator()
    
    # Test assignment and binary operation
    ast = parser.parse("let x = 5 + 3")
    result = generator.generate(ast)
    assert result == 8
    
    # Test using a variable
    ast = parser.parse("x * 2")
    result = generator.generate(ast)
    assert result == 16
