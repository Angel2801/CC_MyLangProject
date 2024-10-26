# src/parser/parser.py
import ply.yacc as yacc
from src.lexer.lexer import tokens

# Define grammar rules

# Rule for assignment expressions
def p_assignment(p):
    'expression : LET IDENTIFIER EQUAL expression'
    p[0] = ('assign', p[2], p[4])

# Rule for binary expressions
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

# Rule for number literals
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('num', p[1])

# Rule for identifiers
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('id', p[1])

# Rule for expressions within parentheses
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
