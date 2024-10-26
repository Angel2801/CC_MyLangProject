import ply.lex as lex
from typing import List, Any

class LexerError(Exception):
    pass

# Extended token set
tokens = (
    'LET', 'FUN', 'IF', 'THEN', 'ELSE', 'MATCH', 'WITH', 'ARROW',
    'IDENTIFIER', 'NUMBER', 'STRING', 'FLOAT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'EQUAL', 'LESS', 'GREATER', 'LEQ', 'GEQ', 'NEQ',
    'AND', 'OR', 'NOT', 'SEMICOLON', 'COMMA'
)

# Regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ARROW = r'->'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='
t_SEMICOLON = r';'
t_COMMA = r','

keywords = {
    'let': 'LET',
    'fun': 'FUN',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'match': 'MATCH',
    'with': 'WITH',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise LexerError(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")

lexer = lex.lex()