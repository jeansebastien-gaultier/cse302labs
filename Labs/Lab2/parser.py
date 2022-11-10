import getopt
import sys
import class_def as CD
from starter_1.starter.py.ply import yacc as yacc
from lexer import Lexer


class Parser(object):
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module = self, start = 'program')

    def parsing(self, text):
        return self.parser.parse(input = text, lexer = self.lexer)

    precedence_BX = (('left', 'BITOR'),('left', 'BITXOR'),('left', 'BITAND'),('left', 'BITSHL', 'BITSHR'),('left', 'PLUS', 'MINUS'),('left', 'TIMES', 'DIV', 'MODULUS'),('right', 'UMINUS'),('right', 'BITCOMPL'))

    def p_err(self, p):
        if p:
            raise SyntaxError(f'Error because sign of {p.type} is wrong')
        else:
            raise SyntaxError (f'Wrong program')

    def p_a(p):
        """a : bstar"""
        p[0] = p[1]

    def p_bstar(p):
        """bstar :
        | bstar b"""
        if len(p) == 1:
        # empty case
            p[0] = []
        else:
        # nonempty case
            p[0] = p[1]
            p[0].append(p[2])

    def p_func(self, p):
        p[0] = p[2]

    def p_program(self, p):
        p[0] = p[5]

    def p_expr_ident(self, p):
        p[0] = CD.ExpressionVar(p[1], p.lineno(1))

    def p_expr_int(self, p):
        p[0] = CD.ExpressionInt(p[1], p.lineno(1))

    def p_expr_parens(self, p):
        p[0] = p[2]

    def p_expr_bin_op(self, p):
        op_to_comp = {'+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIV', '|': 'BITOR', '^': 'BITXOR',  '&': 'BITAND','%': 'MODULUS',  '<<': 'BITSHL','>>': 'BITSHR'}
        p[0] = CD.ExpressionBinOp(p[1],op_to_comp[p[2]] ,p[3], p.lineno)

    def p_expr_uni_op(self, p):
        op_to_comp = {'-': 'UMINUS','~': 'BITCOMPL'}
        p[0] = CD.ExpressionUNiOP(op_to_comp[p[1]], p[2], p.lineno(1))

    def p_statement_var_decl(self, p):
        p[0] = CD.StatementVarDecl(p[2], p[4], p[6], p.lineno(2))

    def p_statement_assign(self, p):
        p[0] = CD.StatementAssign(CD.EXpressionVar(p[1], p.lineno(1)), p[3], lineno=p.lineno(3))
    
    def p_print(self, p):
        p[0] = CD.StatementCall(function="print",  args=[p[3]], lineno=p.lineno(1))

    def p_statement(self, p):
        if len(p) > 1:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = []


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    with open(args[0], 'r') as fp:
        data = fp.read()
    print(data)
    lexer = Lexer()
    parser = Parser()
    p = parser.parse(data)
    print(p)