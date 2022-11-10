import getopt
import sys
from starter_1.starter.py.ply import lex as lex

class Lexer(object):
    def __init__(self, **kwargs):
        self.lexer = lex.lex(object = self, **kwargs)

    keywords = {'print': 'PRINT', 'def': 'DEF','var': 'VAR', 'int': 'INT', 'main': 'MAIN'}

    tokens = ('PLUS', 'MINUS', 'SEMICOLON', 'LPAREN', 'RPAREN', 'IDENT', 'NUMBER','LBRACE', 'RBRACE','BITSHL', 'BITSHR', 'BITXOR', 'BITOR', 'BITAND','TIMES', 'DIV', 'MODULUS', 'UMINUS', 'BITCOMPL','ASSIGN', 'COLON') + tuple(keywords.values())

    def input(self, text):
        self.lexer.input(text)

    def lineno_to_one(self):
        self.lexer.lineno = 1

    def tokens(self):
        self.last_token = self.lexer.tokens()
        return self.last_token

    def token_column(self, token):
        last = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        return token.lexpos - last

    def t_IDENT(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.keywords.get(t.value, 'IDENT')
        return t

    def t_NUMBER(self, t):
        r'0|[1-9][0-9]*'
        t.value = int(t.value)
        if t.value < 0 or t.value >= (1 << 63):
            raise SyntaxError('Number out of range [0, 2^63-1]')
        return t

    def t_COMMENTS(self, t):
        r'//.*\n?'
        t.lexer.lineno += 1

    def t_newline(self, t):
        r'\n'
        t.lexer.lineno += 1

    def t_error(self, t):
        t.lexer.skip(1)
        raise SyntaxError(f'Unknown charackter {t.value[0]}')

    # def test(self, data):
    #     self.input(data)
    #     while True:
    #         tok = self.token()
    #         if tok:
    #             print(tok)
    #         else:
    #             break

    DEF = r'def'
    PLUS = r'\+'
    MINUS = '-'
    TIMES = r'\*'
    DIV = r'\/'
    MODULUS = r'\%'
    ASSIGN = r'\='
    SEMICOLON = ';'
    COLON = ':'
    LPAREN = r'\('
    RPAREN = r'\)'
    BITSHL = r'\<\<'
    BITSHR = r'\>\>'
    BITXOR = r'\^'
    BITOR = r'\|'
    BITAND = r'\&'
    BITCOMPL = r'\~'
    LBRACE = r'\{'
    RBRACE = r'\}'
    ignore = " \t\f\v\r"
    

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    with open(args[0], 'r') as fp:
        data = fp.read()
    print(data)
    lexer = Lexer()
    lexer.test(data)