import getopt
import sys
from py.ply import yacc as yacc
from scanner import Lexer
import json_to_stat as jts


class Parser(object):
    def __init__(self, code, filename=""):
        self.lex = Lexer(filename=filename)
        self.tokens = self.lex.tokens
        self.parser = yacc.yacc(module=self, start='program')
        self.filename = filename
        self.code = code

    def parse(self):
        return self.parser.parse(input=self.code, lexer=self.lex)

    precedence = (
        ('left', 'bor'),
        ('left', 'band'),
        ('left', 'or'),
        ('left', 'xor'),
        ('left', 'and'),
        ('nonassoc', 'jz', 'jnz'),
        ('nonassoc', 'jl', 'jnle', 'jle', 'jnl'),
        ('left', 'shl', 'shr'),
        ('left', 'add', 'sub'),
        ('left', 'mul', 'div', 'mod'),
        ('right', 'neg', 'NOT'),
        ('right', 'not')
    )

    def p_error(self, p):
        if not p:
            print(f'Error: Invalid program')
        else:
            print(f'File "{self.filename}", line {p.lineno}')
            print(f'Error: Unexpected sign "{p.value}"')
        sys.exit(1)

    def p_expr_ident(self, p):
        """expr : IDENT"""
        p[0] = jts.ExpressionVar(p[1], p.lineno(1), self.lex.find_tok_column(p, 1))

    def p_expr_number(self, p):
        """expr : NUMBER"""
        p[0] = jts.ExpressionInt(p[1], p.lineno(1), self.lex.find_tok_column(p, 1))

    def p_expr_bool(self, p):
        """expr : true
                | false"""
        p[0] = jts.ExpressionBool(p[1], p.lineno(1), self.lex.find_tok_column(p, 1))

    def p_expr_binop(self, p):
        '''expr : expr add expr
                | expr sub expr
                | expr mul expr
                | expr div expr
                | expr mod expr
                | expr shr expr
                | expr shl expr
                | expr xor expr
                | expr or expr
                | expr and expr
                | expr bor expr
                | expr band expr
                | expr jz expr
                | expr jnz expr
                | expr jl expr
                | expr jnle expr
                | expr jle expr
                | expr jnl expr'''

        to_name = {'+': 'add', '-': 'sub', '*': 'mul',
                   '/': 'div', '%': 'mod', '>>': 'shr', '<<': 'shl',
                   '^': 'xor', '|': 'or', '&': 'and', '||': 'bor',
                   '&&': 'band', '==': 'jz', '!=': 'jnz', '<': 'jl',
                   '>': 'jnle', '<=': 'jle', '>=': 'jnl'}

        p[0] = jts.ExpressionBinOp(p[1], to_name[p[2]], p[3], p.lineno(2), self.lex.find_tok_column(p, 1))

    def p_expr_unop(self, p):
        '''expr : not expr
                | sub expr %prec neg
                | neg expr
                | NOT expr'''

        to_name = {'-': 'neg', '~': 'not', '!': 'NOT'}
        p[0] = jts.ExpressionUniOp(to_name[p[1]], p[2], p.lineno(1), self.lex.find_tok_column(p, 1))

    def p_expr_parens(self, p):
        '''expr : LPAREN expr RPAREN'''
        p[0] = p[2]

    def p_block(self, p):
        '''block : LBRACE stmts RBRACE'''
        p[0] = jts.StatementBlock(p[2])

    def p_decl_type(self, p):
        '''type : INT
                | BOOL'''
        p[0] = p[1].lower()

    def p_vardecl(self, p):
        '''stmt : VAR IDENT ASSIGN expr COLON type SEMICOLON'''
        p[0] = jts.StatementVarDecl(p[2], p[4], p[6], p.lineno(2))

    def p_assign(self, p):
        '''stmt : IDENT ASSIGN expr SEMICOLON'''
        p[0] = jts.StatementAssign(jts.ExpressionVar(p[1], p.lineno(1)),
                          p[3], lineno=p.lineno(3))

    def p_continue(self, p):
        '''stmt : CONTINUE SEMICOLON'''
        p[0] = jts.StructuredJump(jump_type="continue", lineno=p.lineno(1))

    def p_break(self, p):
        '''stmt : BREAK SEMICOLON'''
        p[0] = jts.StructuredJump(jump_type="break", lineno=p.lineno(1))

    def p_print(self, p):
        '''stmt : PRINT LPAREN expr RPAREN SEMICOLON'''
        p[0] = jts.StatementCall(function="print",  args=[p[3]], lineno=p.lineno(1))

    def p_ifelse(self, p):
        '''ifelse : IF LPAREN expr RPAREN block ifrest'''
        p[0] = jts.StatementIf(p[3], p[5], p[6], lineno=p.lineno(1))

    def p_ifrest(self, p):
        '''ifrest : ELSE ifelse
                | ELSE block
                |'''
        if len(p) == 1:
            p[0] = None
        else:
            p[0] = p[2]

    def p_while(self, p):
        '''while : WHILE LPAREN expr RPAREN block'''
        p[0] = jts.StatementWhile(p[3], p[5], lineno=p.lineno(1))

    def p_stmt(self, p):
        '''stmts : stmt stmts
                | while stmts
                | ifelse stmts
                |'''
        p[0] = [p[1]] + p[2] if len(p) > 1 else []

    def p_program(self, p):
        '''program : def MAIN LPAREN RPAREN block'''
        p[0] = p[5]

