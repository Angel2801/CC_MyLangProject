# src/lexer/tokens.py

# Define the tokens as a tuple
tokens = (
    'LET', 'FUN', 'IF', 'THEN', 'ELSE', 'MATCH', 'WITH', 'ARROW',
    'IDENTIFIER', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

# Define regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ARROW = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define more complex tokens as functions
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Error handling function
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
