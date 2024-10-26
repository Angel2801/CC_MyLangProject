from dataclasses import dataclass
from typing import Any, Optional, List

@dataclass
class Position:
    line: int
    column: int

class ASTNode:
    def __init__(self):
        self.position: Optional[Position] = None
        self.type: Optional[str] = None

@dataclass
class AssignmentNode(ASTNode):
    identifier: str
    value: ASTNode
    type_annotation: Optional[str] = None

@dataclass
class FunctionNode(ASTNode):
    name: str
    params: List[str]
    body: ASTNode
    return_type: Optional[str] = None

@dataclass
class BinaryOperationNode(ASTNode):
    operator: str
    left: ASTNode
    right: ASTNode

@dataclass
class UnaryOperationNode(ASTNode):
    operator: str
    operand: ASTNode

@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_branch: ASTNode
    else_branch: Optional[ASTNode]

@dataclass
class NumberNode(ASTNode):
    value: Any

@dataclass
class StringNode(ASTNode):
    value: str

@dataclass
class IdentifierNode(ASTNode):
    name: str