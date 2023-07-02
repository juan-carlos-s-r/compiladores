from TipoToken import * #importaciones de las classes
from Token import *

class parser:
    index=0

    def siguiente(self):
        global index
        self.index+=1
        if self.i < len(Token.tokens):
            self.token_actual=Token.tokens[0][index][0]
        else:
            self.token_actual=None

    def igualar(self,token_esperado):
        if self.token_actual==token_esperado:
            self.siguiente()
        else:
            print(f"Syntax error se esperaba {token_esperado} se encontro {self.token_actual}")

    def program(self):
        self.declaration()

    def declaration(self):
        if self.token_actual == 'class':
            self.class_decl()
        elif self.token_actual == 'fun':
            self.fun_decl()
        elif self.token_actual == 'var':
            self.var_decl()
        elif self.token_actual in ['print', 'return', 'while', 'for', 'if', '{', 'id']:
            self.statement()

    def class_decl(self):
        self.igualar('class')
        self.igualar('id')
        self.class_inher()
        self.igualar('{')
        self.functions()
        self.match('}')

    def class_inher(self):
        if self.token_actual=='<':
            self.igualar('<')
            self.igualar('id')

    def fun_decl(self):
        self.igualar('fun')
        self.function()

    def var_decl(self):
        self.igualar('var')
        self.igualar('id')
        self.var_init()
        self.igualar(';')

    def var_init(self):
        if self.token_actual=='=':
            self.igualar('=')
            self.expression()
    
    def statement(self):
        if self.token_actual == 'print':
            self.print_stmt()
        elif self.token_actual == 'return':
            self.return_stmt()
        elif self.token_actual == 'while':
            self.while_stmt()
        elif self.token_actual == 'for':
            self.for_stmt()
        elif self.token_actual == 'if':
            self.if_stmt()
        elif self.token_actual == '{':
            self.block()
        elif self.token_actual == 'id':
            self.expr_stmt()
        
    def print_stmt(self):
        self.igualar('print')
        self.expression()
        self.igualar(';')
    
    def return_stmt(self):
        self.igualar('return')
        self.return_exp_opc()
        self.igualar(';')

    def return_exp_opc(self):
        if self.token_actual != ';':
            self.expression()
        else:pass

    def while_stmt(self):
        self.igualar('while')
        self.igualar('(')
        self.expression()
        self.igualar(')')
        self.statement()

#fijarse si funciona bien
    def for_stmt(self):
        self.igualar('for')
        self.igualar('(')
        if self.token_actual == 'var':
            self.var_decl()
        else:
            self.expr_stmt()
        self.expression()
        self.igualar(';')
        if self.token_actual != ')':
            self.expression()
        self.igualar(')')
        self.statement()

    def if_stmt(self):
        self.igualar('if')
        self.igualar('(')
        self.expression()
        self.igualar(')')
        self.statement()
        if self.token_actual == 'else':
            self.igualar('else')
            self.statement()

    def block(self):
        self.igualar('{')
        while self.token_actual != '}':
            self.declaration()
        self.igualar('}')

    def expression(self):
        self.assignment()

    def assignment(self):
        self.logic_or()
        if self.token_actual == '=':
            self.igualar('=')
            self.expression()

    def logic_or(self):
        self.logic_and()
        self.logic_or2()

    def logic_or2(self):
        if self.token_actual == 'or':
            self.igualar('or')
            self.logic_and()
            self.logic_or2()

    def logic_and(self):
        self.equality()
        self.logic_and2()

    def logic_and2(self):
        if self.token_actual == 'and':
            self.igualar('and')
            self.equality()
            self.logic_and2()

    def equality(self):
        self.comparison()
        self.equality2()

    def equality2(self):
        if self.token_actual in ['==', '!=']:
            if self.token_actual == '==':
                self.igualar('==')
                self.comparison()
                self.equality2()
            else:
                self.igualar('!=')
                self.comparison()
                self.equality2()
    
    def comparison(self):
        self.term()
        self.comparison2()

    def comparison2(self):
        if self.token_actual in ['<', '>', '<=', '>=']:
            if self.token_actual == '<':
                self.igualar('<')
            elif self.token_actual == '>':
                self.igualar('>')
            elif self.token_actual == '<=':
                self.igualar('<=')
            else:
                self.igualar('>=')
            self.term()
            self.comparison2

    def term(self):
        self.factor()
        self.term2()

    def term2(self):
        if self.token_actual in ['+', '-']:
            if self.token_actual == '+':
                self.igualar('+')
            else:
                self.igualar('-')
            self.factor()
            self.term2

    def factor(self):
        self.unary()
        self.factor2()

    def factor2(self):
        if self.token_actual in ['*', '/']:
            if self.token_actual == '*':
                self.igualar('*')
            else:
                self.igualar('/')
            self.unary()
            self.factor2()

    def unary(self):
        if self.token_actual in ['!', '-']:
            if self.token_actual == '!':
                self.igualar('!')
            else:
                self.igualar('-')
            self.unary()
        else:
            self.call()
    
    def call(self):
        self.primary()
        self.call_2()

    def call_2(self):
        if self.token_actual in ['(', '.']:
            if self.token_actual == '(':
                self.igualar('(')
                if self.token_actual != ')':
                    self.arguments()
                self.igualar(')')
                self.call_2
            elif self.token_actual == '.':
                self.igualar('.')
                self.igualar('id')
                self.call_2
    
    def primary(self):
        if self.token_actual in ['true', 'false', 'null', 'this', 'number', 'string', 'id']:
            self.igualar(self.token_actual)
        elif self.token_actual == '(':
            self.igualar('(')
            self.expression()
            self.igualar(')')
        elif self.token_actual == 'super':
            self.igualar('super')
            self.igualar('.')
            self.igualar('id')

    def function(self):
        self.igualar('id')
        self.igualar('(')
        if self.token_actual != ')':
            self.parameters()
        self.igualar(')')
        self.block()

    def functions(self):
        if self.token_actual != '}':
            self.function()
            self.functions()

    def parameters(self):
        self.igualar('id')
        self.parameters_2()

    def parameters_2(self):
        if self.token_actual == ',':
            self.igualar(',')
            self.igualar('id')
            self.parameters_2()
    
    def arguments(self):
        self.expression()
        self.arguments_2()
    
    def arguments_2(self):
        if self.token_actual == ',':
            self.igualar(',')
            self.expression()
            self.arguments_2()

    
print("ASDR Terminado")