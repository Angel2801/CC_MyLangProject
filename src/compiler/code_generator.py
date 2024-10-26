from typing import Dict, Any
from src.ast.nodes import *

class CodeGenerationError(Exception):
    pass

class CodeGenerator:
    def __init__(self):
        self.environment: Dict[str, Any] = {}
        self.functions: Dict[str, FunctionNode] = {}
        
    def generate(self, node: ASTNode) -> Any:
        if isinstance(node, AssignmentNode):
            value = self.generate(node.value)
            self.environment[node.identifier] = value
            return value
            
        elif isinstance(node, FunctionNode):
            self.functions[node.name] = node
            return None
            
        elif isinstance(node, BinaryOperationNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            
            ops = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y,
                '%': lambda x, y: x % y,
                '<': lambda x, y: x < y,
                '>': lambda x, y: x > y,
                '<=': lambda x, y: x <= y,
                '>=': lambda x, y: x >= y,
                '==': lambda x, y: x == y,
                '!=': lambda x, y: x != y,
            }
            
            if node.operator not in ops:
                raise CodeGenerationError(f"Unknown operator: {node.operator}")
                
            return ops[node.operator](left, right)
            
        elif isinstance(node, IfNode):
            condition = self.generate(node.condition)
            if condition:
                return self.generate(node.then_branch)
            elif node.else_branch:
                return self.generate(node.else_branch)
            return None
            
        elif isinstance(node, NumberNode):
            return node.value
            
        elif isinstance(node, StringNode):
            return node.value
            
        elif isinstance(node, IdentifierNode):
            if node.name not in self.environment:
                raise CodeGenerationError(f"Undefined variable: {node.name}")
            return self.environment[node.name]
            
        raise CodeGenerationError(f"Unknown node type: {type(node)}")