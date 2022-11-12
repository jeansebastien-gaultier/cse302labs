import getopt
import sys
from py.ply import lex 


class Lexer(object):
    def __init__(self, filename, **kwargs):
        self.filename = filename
        self.lexer = lex.lex(object=self, **kwargs)

    def input(self, text):
        self.lexer.input(text)

    def reset_lineno(self):
        self.lexer.lineno = 1

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token

    def find_tok_column(self, token):
        last_cr = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        return token.lexpos - last_cr

    keywords = {'print': 'PRINT', 'def': 'def', 'true': 'true', 'false': 'false',
                'var': 'VAR', 'bool': 'BOOL', 'int': 'INT', 'main': 'MAIN',
                'if': 'IF', 'else': 'ELSE',
                'while': 'WHILE',
                'break': 'BREAK', 'continue': 'CONTINUE'}

    tokens = (
        'add', 'sub', 'SEMICOLON', 'LPAREN', 'RPAREN', 'IDENT', 'NUMBER',
        'LBRACE', 'RBRACE',
        'shl', 'shr', 'xor', 'or', 'and',
        'mul', 'div', 'mod', 'neg', 'not',
        'ASSIGN', 'COLON', 'bor', 'band', 'jz', 'jnz',
        'jl', 'jnle', 'jle', 'jnl', 'NOT'
    ) + tuple(keywords.values())

    t_def = r'def'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_add = r'\+'
    t_sub = '-'
    t_SEMICOLON = ';'
    t_shr = r'\>\>'
    t_shl = r'\<\<'
    t_xor = r'\^'
    t_or = r'\|'
    t_and = r'\&'
    t_mul = r'\*'
    t_div = r'\/'
    t_mod = r'\%'
    t_not = r'\~'
    t_ASSIGN = r'\='
    t_COLON = ':'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_bor = r'\|\|'
    t_band = r'\&\&'
    t_jz = r'\=\='
    t_jnz = r'\!\='
    t_jl = r'\<'
    t_jle = r'\<\='
    t_jnle = r'\>'
    t_jnl = r'\>\='
    t_NOT = r'\!'

    t_ignore = " \t\f\v\r"

    def t_IDENT(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.keywords.get(t.value, 'IDENT')
        return t

    def t_NUMBER(self, t):
        r'0|[1-9][0-9]*'
        t.value = int(t.value)

        if t.value < 0 or t.value >= (1 << 63):
            errorS(self.filename, "outRange", t.lexer, t.value)

        return t

    def t_COMMENTS(self, t):
        r'//.*\n?'
        t.lexer.lineno += 1

    def t_newline(self, t):
        r'\n'
        t.lexer.lineno += 1

    def t_error(self, t):
        errorS(self.filename, "unexpChar", t.lexer, t.value[0])

def errorS(filename, err, val1, val2):
    print(f'File "{filename}", line {val1.lineno}')
    if err == "outRange":
        print(f'Error: Integer "{val2}" out of range')
    elif err == "unexpChar":
        print(f'Error: Unexpected character "{val2}"')
    sys.exit(1)