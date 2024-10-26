# src/lexer/tests/test_lexer.py
from src.lexer.lexer import lexer

def test_lexer():
    data = "let x = 5 + 3"
    lexer.input(data)
    token_list = [(token.type, token.value) for token in lexer]
    
    expected_tokens = [
        ('LET', 'let'),
        ('IDENTIFIER', 'x'),
        ('EQUAL', '='),
        ('NUMBER', 5),
        ('PLUS', '+'),
        ('NUMBER', 3)
    ]
    
    assert token_list == expected_tokens
