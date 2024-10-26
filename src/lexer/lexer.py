# src/lexer/lexer.py
import ply.lex as lex

# Token names
tokens = (
    'LET', 'FUN', 'IF', 'THEN', 'ELSE', 'MATCH', 'WITH', 'ARROW',
    'IDENTIFIER', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'EQUAL'
)

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ARROW = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='

# Keywords dictionary to differentiate keywords from identifiers
keywords = {
    'let': 'LET',
    'fun': 'FUN',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'match': 'MATCH',
    'with': 'WITH'
}

# Function for identifiers and keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Check for keywords
    return t

# Function for number tokens
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling function
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
