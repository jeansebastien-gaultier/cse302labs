import sys, getopt
from json_to_stat import *
from myParser import Parser

def bx2front(code, filename='', flag = False):
    parser = Parser(code, filename)
    try:
        instructions = parser.parse()
        for inst in instructions:
            if isinstance(inst, ProcDec):
                if inst.name in scopes[0]:
                    raise SyntaxError('Proc Redeclaration')
                if inst.name == 'main':
                    if inst.type !='void':
                        raise SyntaxError('Invalid type')
                    flag = True
                scopes[0][inst.name] = (inst.type, inst.lineno, [arg.type for arg in inst.args])
            else:
                for i in inst:
                    if i.name in scopes[0]:
                        raise SyntaxError('Variable Redeclaration')
                    if isinstance(i.initial, ExpressionInt) == False:
                        if i.type == 'int':
                            raise SyntaxError ('Invalid declaration')
                    if isinstance(i.initial, ExpressionBool):
                        if i.type == 'bool':
                            raise SyntaxError('Invalid declaration')
                    scopes[0][i.name] = (i.type, i.lineno)

        if flag == True:
            raise SyntaxError('Missing main function')
        for inst in instructions:
            if isinstance(inst, ProcDec) == True:
                inst.type_check()
    except SyntaxError as err:
        print('Syntax error:', err)
        sys.exit(1)
    scopes.pop()
    scopes.append(dict())
    return instructions


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    filename = args[0]

    with open(filename, 'r') as file:
        code = file.read()

    bx2front(code, filename)
    scopes
