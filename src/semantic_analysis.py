# src/semantic_analysis.py
from src.ast.nodes import AssignmentNode, IdentifierNode

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = set()

    def analyze(self, node):
        if isinstance(node, AssignmentNode):
            self.symbol_table.add(node.identifier)
            self.analyze(node.value)
        elif isinstance(node, IdentifierNode):
            if node.name not in self.symbol_table:
                raise NameError(f"Undefined variable '{node.name}'")
        elif hasattr(node, 'left') and hasattr(node, 'right'):  # BinaryOperationNode
            self.analyze(node.left)
            self.analyze(node.right)
        elif hasattr(node, 'value'):  # NumberNode
            pass
