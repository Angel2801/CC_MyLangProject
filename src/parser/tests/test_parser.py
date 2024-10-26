# src/parser/tests/test_parser.py
from src.parser.parser import parser

def test_parser():
    # Test an assignment
    result = parser.parse("let x = 5 + 3")
    expected_result = ('assign', 'x', ('binop', '+', ('num', 5), ('num', 3)))
    assert result == expected_result

    # Test a simple binary expression
    result = parser.parse("5 * (2 + 3)")
    expected_result = ('binop', '*', ('num', 5), ('binop', '+', ('num', 2), ('num', 3)))
    assert result == expected_result
