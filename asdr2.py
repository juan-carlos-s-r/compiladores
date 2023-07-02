class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.advance()
        else:
            raise Exception(f"Syntax error. Expected {expected_token}, found {self.current_token}")

    def program(self):
        self.declaration()

    def declaration(self):
        if self.current_token == 'class':
            self.class_decl()
        elif self.current_token == 'fun':
            self.fun_decl()
        elif self.current_token == 'var':
            self.var_decl()
        elif self.current_token in ['print', 'return', 'while', 'for', 'if', '{', 'id']:
            self.statement()

    def class_decl(self):
        self.match('class')
        self.match('id')
        self.class_inher()
        self.match('{')
        self.functions()
        self.match('}')

    def class_inher(self):
        if self.current_token == '<':
            self.match('<')
            self.match('id')

    def fun_decl(self):
        self.match('fun')
        self.function()

    def var_decl(self):
        self.match('var')
        self.match('id')
        if self.current_token == '=':
            self.match('=')
            self.expression()
        self.match(';')

    def statement(self):
        if self.current_token == 'print':
            self.print_stmt()
        elif self.current_token == 'return':
            self.return_stmt()
        elif self.current_token == 'while':
            self.while_stmt()
        elif self.current_token == 'for':
            self.for_stmt()
        elif self.current_token == 'if':
            self.if_stmt()
        elif self.current_token == '{':
            self.block()
        elif self.current_token == 'id':
            self.expr_stmt()

    def print_stmt(self):
        self.match('print')
        self.expression()
        self.match(';')

    def return_stmt(self):
        self.match('return')
        if self.current_token != ';':
            self.expression()
        self.match(';')

    def while_stmt(self):
        self.match('while')
        self.match('(')
        self.expression()
        self.match(')')
        self.statement()

    def for_stmt(self):
        self.match('for')
        self.match('(')
        if self.current_token == 'var':
            self.var_decl()
        else:
            self.expr_stmt()
        self.expression()
        self.match(';')
        if self.current_token != ')':
            self.expression()
        self.match(')')
        self.statement()

    def if_stmt(self):
        self.match('if')
        self.match('(')
        self.expression()
        self.match(')')
        self.statement()
        if self.current_token == 'else':
            self.match('else')
            self.statement()

    def block(self):
        self.match('{')
        while self.current_token != '}':
            self.declaration()
        self.match('}')

    def expression(self):
        self.assignment()

    def assignment(self):
        self.logic_or()
        if self.current_token == '=':
            self.match('=')
            self.expression()

    def logic_or(self):
        self.logic_and()
        while self.current_token == 'or':
            self.match('or')
            self.logic_and()

    def logic_and(self):
        self.equality()
        while self.current_token == 'and':
            self.match('and')
            self.equality()

    def equality(self):
        self.comparison()
        while self.current_token in ['==', '!=']:
            if self.current_token == '==':
                self.match('==')
            else:
                self.match('!=')
            self.comparison()

    def comparison(self):
        self.term()
        while self.current_token in ['<', '>', '<=', '>=']:
            if self.current_token == '<':
                self.match('<')
            elif self.current_token == '>':
                self.match('>')
            elif self.current_token == '<=':
                self.match('<=')
            else:
                self.match('>=')
            self.term()

    def term(self):
        self.factor()
        while self.current_token in ['+', '-']:
            if self.current_token == '+':
                self.match('+')
            else:
                self.match('-')
            self.factor()

    def factor(self):
        self.unary()
        while self.current_token in ['*', '/']:
            if self.current_token == '*':
                self.match('*')
            else:
                self.match('/')
            self.unary()

    def unary(self):
        if self.current_token in ['!', '-']:
            if self.current_token == '!':
                self.match('!')
            else:
                self.match('-')
            self.unary()
        else:
            self.call()

    def call(self):
        self.primary()
        while self.current_token in ['(', '.']:
            if self.current_token == '(':
                self.match('(')
                if self.current_token != ')':
                    self.arguments()
                self.match(')')
            elif self.current_token == '.':
                self.match('.')
                self.match('id')

    def primary(self):
        if self.current_token in ['true', 'false', 'null', 'this', 'number', 'string', 'id']:
            self.match(self.current_token)
        elif self.current_token == '(':
            self.match('(')
            self.expression()
            self.match(')')
        elif self.current_token == 'super':
            self.match('super')
            self.match('.')
            self.match('id')

    def function(self):
        self.match('id')
        self.match('(')
        if self.current_token != ')':
            self.parameters()
        self.match(')')
        self.block()

    def functions(self):
        if self.current_token != '}':
            self.function()
            self.functions()

    def parameters(self):
        self.match('id')
        while self.current_token == ',':
            self.match(',')
            self.match('id')

    def arguments(self):
        self.expression()
        while self.current_token == ',':
            self.match(',')
            self.expression()


# Example usage
tokens = ['class', 'MyClass', '{', 'fun', 'myFunction', '(', 'param1', ',', 'param2', ')', '{', 'print', 'param1', ';', '}', '}']
parser = Parser(tokens)
parser.program()
