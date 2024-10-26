# tests/test_semantic_analysis.py
from src.parser.parser import parser
from src.semantic_analysis import SemanticAnalyzer

def test_semantic_analysis():
    analyzer = SemanticAnalyzer()
    
    # Valid case: defined variable
    ast = parser.parse("let x = 5 + 3")
    analyzer.analyze(ast)  # Should not raise an error

    # Invalid case: undefined variable
    ast = parser.parse("y + 2")
    try:
        analyzer.analyze(ast)
        assert False, "Expected NameError for undefined variable 'y'"
    except NameError as e:
        assert str(e) == "Undefined variable 'y'"
