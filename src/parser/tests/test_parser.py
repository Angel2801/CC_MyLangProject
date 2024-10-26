# src/parser/tests/test_parser.py
from src.parser.parser import parser
from src.ast.nodes import AssignmentNode, BinaryOperationNode, NumberNode, IdentifierNode

def test_parser():
    # Test an assignment
    result = parser.parse("let x = 5 + 3")
    expected_result = AssignmentNode("x", BinaryOperationNode("+", NumberNode(5), NumberNode(3)))
    assert repr(result) == repr(expected_result)

    # Test a simple binary expression
    result = parser.parse("5 * (2 + 3)")
    expected_result = BinaryOperationNode("*", NumberNode(5), BinaryOperationNode("+", NumberNode(2), NumberNode(3)))
    assert repr(result) == repr(expected_result)
