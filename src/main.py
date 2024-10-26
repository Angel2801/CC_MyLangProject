import unittest
from src.lexer.lexer import lexer, LexerError
from src.parser.parser import parser
from src.semantic_analysis import SemanticAnalyzer, SemanticError
from src.compiler.code_generator import CodeGenerator, CodeGenerationError

class LanguageTests(unittest.TestCase):
    def setUp(self):
        self.analyzer = SemanticAnalyzer()
        self.generator = CodeGenerator()

    def test_lexer(self):
        """Test lexical analysis"""
        # Test 1: Basic tokens
        code = "let x = 5 + 3"
        lexer.input(code)
        tokens = [token.type for token in lexer]
        self.assertEqual(tokens, ['LET', 'IDENTIFIER', 'EQUAL', 'NUMBER', 'PLUS', 'NUMBER'])

        # Test 2: Keywords
        code = "if x then y else z"
        lexer.input(code)
        tokens = [token.type for token in lexer]
        self.assertEqual(tokens, ['IF', 'IDENTIFIER', 'THEN', 'IDENTIFIER', 'ELSE', 'IDENTIFIER'])

        # Test 3: Special characters
        code = "x <= y >= z != w"
        lexer.input(code)
        tokens = [token.type for token in lexer]
        self.assertEqual(tokens, ['IDENTIFIER', 'LEQ', 'IDENTIFIER', 'GEQ', 'IDENTIFIER', 'NEQ', 'IDENTIFIER'])

        # Test 4: Numbers and strings
        code = 'let x = 3.14 let y = "hello"'
        lexer.input(code)
        tokens = [(token.type, token.value) for token in lexer]
        expected = [
            ('LET', 'let'),
            ('IDENTIFIER', 'x'),
            ('EQUAL', '='),
            ('FLOAT', 3.14),
            ('LET', 'let'),
            ('IDENTIFIER', 'y'),
            ('EQUAL', '='),
            ('STRING', 'hello')
        ]
        self.assertEqual(tokens, expected)

        # Test 5: Invalid characters
        with self.assertRaises(LexerError):
            code = "let x = @"
            lexer.input(code)
            list(lexer)

    def test_parser(self):
        """Test parsing functionality"""
        # Test 1: Basic assignment
        code = "let x = 5"
        ast = parser.parse(code)
        self.assertIsInstance(ast, AssignmentNode)
        self.assertEqual(ast.identifier, 'x')

        # Test 2: Binary operations
        code = "let x = 5 + 3 * 2"
        ast = parser.parse(code)
        self.assertIsInstance(ast.value, BinaryOperationNode)

        # Test 3: Complex expressions
        code = "if (x > 0) then y + 1 else y - 1"
        ast = parser.parse(code)
        self.assertIsInstance(ast, IfNode)

        # Test 4: Invalid syntax
        with self.assertRaises(SyntaxError):
            code = "let x = +"
            parser.parse(code)

    def test_semantic_analyzer(self):
        """Test semantic analysis"""
        # Test 1: Variable declaration and use
        code = """
        let x = 5;
        let y = x + 3
        """
        ast = parser.parse(code)
        self.analyzer.analyze(ast)

        # Test 2: Type mismatch
        with self.assertRaises(SemanticError):
            code = """
            let x: int = "hello";
            """
            ast = parser.parse(code)
            self.analyzer.analyze(ast)

        # Test 3: Undefined variable
        with self.assertRaises(SemanticError):
            code = "let y = z + 1"
            ast = parser.parse(code)
            self.analyzer.analyze(ast)

        # Test 4: Invalid operation
        with self.assertRaises(SemanticError):
            code = """
            let x = "hello";
            let y = x + 5
            """
            ast = parser.parse(code)
            self.analyzer.analyze(ast)

    def test_code_generator(self):
        """Test code generation and execution"""
        # Test 1: Basic arithmetic
        code = """
        let x = 5;
        let y = 3;
        let z = x + y
        """
        ast = parser.parse(code)
        self.analyzer.analyze(ast)
        result = self.generator.generate(ast)
        self.assertEqual(result, 8)

        # Test 2: Conditional execution
        code = """
        let x = 10;
        if x > 5 then x * 2 else x / 2
        """
        ast = parser.parse(code)
        self.analyzer.analyze(ast)
        result = self.generator.generate(ast)
        self.assertEqual(result, 20)

        # Test 3: String operations
        code = """
        let greeting = "Hello";
        let name = "World";
        let message = greeting + " " + name
        """
        ast = parser.parse(code)
        self.analyzer.analyze(ast)
        result = self.generator.generate(ast)
        self.assertEqual(result, "Hello World")

    def test_edge_cases(self):
        """Test edge cases and error conditions"""
        # Test 1: Division by zero
        with self.assertRaises(CodeGenerationError):
            code = "let x = 5 / 0"
            ast = parser.parse(code)
            self.analyzer.analyze(ast)
            self.generator.generate(ast)

        # Test 2: Nested expressions
        code = """
        let x = 1;
        let y = 2;
        let z = 3;
        let result = (x + y) * (z - x) / (y + z)
        """
        ast = parser.parse(code)
        self.analyzer.analyze(ast)
        result = self.generator.generate(ast)
        self.assertIsInstance(result, (int, float))

        # Test 3: Maximum recursion
        with self.assertRaises(RecursionError):
            code = """
            let x = 1;
            fun factorial(n) {
                if n <= 1 then 1 else n * factorial(n-1)
            };
            factorial(1000)
            """
            ast = parser.parse(code)
            self.analyzer.analyze(ast)
            self.generator.generate(ast)

    def test_integration(self):
        """Integration tests for the complete pipeline"""
        # Test 1: Complete program
        program = """
        let x = 5;
        let y = 3;
        let z = x + y;
        if z > 7 then
            z * 2
        else
            z / 2
        """
        
        # Process the program
        try:
            ast = parser.parse(program)
            self.analyzer.analyze(ast)
            result = self.generator.generate(ast)
            self.assertEqual(result, 16)  # (5 + 3) * 2
        except Exception as e:
            self.fail(f"Integration test failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()