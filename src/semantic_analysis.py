from typing import Dict, Set, Optional
from src.ast.nodes import *

class SemanticError(Exception):
    pass

class Type:
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    FUNCTION = "function"

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table: Dict[str, Dict] = {}
        self.current_scope: List[str] = ["global"]
        
    def enter_scope(self, scope_name: str):
        self.current_scope.append(scope_name)
        
    def exit_scope(self):
        self.current_scope.pop()
        
    def current_scope_name(self) -> str:
        return ".".join(self.current_scope)
    
    def analyze(self, node: ASTNode) -> Optional[str]:
        if isinstance(node, AssignmentNode):
            value_type = self.analyze(node.value)
            if node.type_annotation and node.type_annotation != value_type:
                raise SemanticError(f"Type mismatch: expected {node.type_annotation}, got {value_type}")
            self.symbol_table[node.identifier] = {
                "type": value_type,
                "scope": self.current_scope_name()
            }
            return value_type
            
        elif isinstance(node, BinaryOperationNode):
            left_type = self.analyze(node.left)
            right_type = self.analyze(node.right)
            
            if node.operator in {'+', '-', '*', '/', '%'}:
                if left_type not in {Type.INT, Type.FLOAT} or right_type not in {Type.INT, Type.FLOAT}:
                    raise SemanticError(f"Invalid types for arithmetic operation: {left_type}, {right_type}")
                return Type.FLOAT if Type.FLOAT in {left_type, right_type} else Type.INT
                
            elif node.operator in {'<', '>', '<=', '>=', '==', '!='}:
                if left_type != right_type:
                    raise SemanticError(f"Cannot compare different types: {left_type} and {right_type}")
                return Type.BOOL
                
        elif isinstance(node, IfNode):
            cond_type = self.analyze(node.condition)
            if cond_type != Type.BOOL:
                raise SemanticError(f"Condition must be boolean, got {cond_type}")
            
            then_type = self.analyze(node.then_branch)
            if node.else_branch:
                else_type = self.analyze(node.else_branch)
                if then_type != else_type:
                    raise SemanticError(f"If-then-else branches must have same type: {then_type} != {else_type}")
            return then_type
            
        elif isinstance(node, NumberNode):
            return Type.INT if isinstance(node.value, int) else Type.FLOAT
            
        elif isinstance(node, StringNode):
            return Type.STRING
            
        elif isinstance(node, IdentifierNode):
            if node.name not in self.symbol_table:
                raise SemanticError(f"Undefined variable '{node.name}'")
            return self.symbol_table[node.name]["type"]
        
        return None