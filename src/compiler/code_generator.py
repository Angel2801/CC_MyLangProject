# src/compiler/code_generator.py
from src.ast.nodes import AssignmentNode, BinaryOperationNode, NumberNode, IdentifierNode

class CodeGenerator:
    def __init__(self):
        self.environment = {}

    def generate(self, node):
        if isinstance(node, AssignmentNode):
            value = self.generate(node.value)
            self.environment[node.identifier] = value
            return value
        elif isinstance(node, BinaryOperationNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                return left / right
        elif isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, IdentifierNode):
            return self.environment.get(node.name, None)
