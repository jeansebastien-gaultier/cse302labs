"""
Jean-Sebastien Gaultier

LAB 2: Convert from BX to TAC

The idea is to build both a Lexer and a Parser
"""

import sys
import json
import getopt
from class_def import *
from parser import Parser

filename = ''
variables = {}
linedec = {}
fresh_temp = 0
OP_CONVERTER = {"PLUS": "add", "MINUS": "sub", "TIMES": "mul", "DIV": "div", "MODULUS": "mod", "BITAND": "and", "BITOR": "or", "BITXOR": "xor",
                    "BITSHL": "shl", "BITSHR": "shr", "UMINUS": "neg", "BITCOMPL": "not"}


def tmm_expr(expr, tac):
    global fresh_temp, variables, OP_CONVERTER

    if isinstance(expr, ExpressionInt):
        return "const", [expr.value]

    elif isinstance(expr, ExpressionVar):
        # Added the ERROR compared to the Lab 1 implementation
        if expr.name not in variables:
            print(f'{filename}: line {expr.lineno}:Error:Use of undeclared variable "{expr.name}"')
            sys.exit(1)
        return "copy", [variables[expr.name]]

    elif isinstance(expr, ExpressionBinOp):
        args1 = f'%{str(fresh_temp)}'
        fresh_temp += 1
        op, args = tmm_expr(expr.argument_l, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": args1})
        args2 = f'%{str(fresh_temp)}'
        fresh_temp += 1
        op, args = tmm_expr(expr.argument_r, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": args2})
        return OP_CONVERTER[expr.operator], [args1, args2]

    elif isinstance(expr, ExpressionUniOp):
        args1 = f'%{str(fresh_temp)}'
        fresh_temp += 1
        op, args = tmm_expr(expr.argument, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": args1})
        return OP_CONVERTER[expr.operator], [args1]

    else:
        raise ValueError(f'Unrecognized expression type {expr}')

def tmm_statements(instructions, tac):
    global fresh_temp, variables, filename

    for inst in instructions:
        if isinstance(inst, StatementVarDecl):
            # Added the ERROR compared to the Lab 1 implementation
            if inst.name in variables:
                print(f'{filename}:line {inst.lineno}:Error:Duplicate declaration of variable "{inst.name}"')
                print(f'{filename}:line {linedec[inst.name]}:Info:Earlier declaration of "{inst.name}"')
                sys.exit(1)
            result = f'%{str(fresh_temp)}'
            fresh_temp += 1
            op, args = tmm_expr(inst.init, tac)
            linedec[inst.name] = inst.lineno
            variables[inst.name] = result
            tac[0]["body"].append({"opcode": op, "args": args, "result": result})

        elif isinstance(inst, StatementAssign):
            # Added the ERROR compared to the Lab 1 implementation
            if inst.target.name not in variables:
                print(f'{filename}: line {inst.target.lineno}:Error:Assigning an undeclared variable "{inst.target.name}"')
                sys.exit(1)
            result = variables[inst.target.name]

            op, args = tmm_expr(inst.expr, tac)
            tac[0]["body"].append({"opcode": op, "args": args, "result": result})

        elif isinstance(inst, StatementCall):
            result = f'%{str(fresh_temp)}'
            fresh_temp += 1
            op, args = tmm_expr(inst.arguments[0], tac)
            tac[0]["body"].append({"opcode": op, "args": args, "result": result})
            tac[0]["body"].append({"opcode": inst.func, "args": [result], "result": None})

        else:
            raise ValueError(f'Unrecognized statement form: {inst}')

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    filename = args[0]

    if not filename.endswith('.bx'):
        raise TypeError(f'The file {filename} is not a BX file, it will not work')

    with open(filename, 'r') as file:
        code = file.read()

    parser = Parser()

    try:
        inst = parser.parse(code)
    except SyntaxError as err:
        print('Syntax error:', err)
        sys.exit(1)

    tac = [{"proc": "@main", "body": []}]

    tmm_statements(inst, tac)

    tac_json = json.dumps(tac)
    with open(filename.split('\\')[-1].split('.')[0] + '.tac.json', 'w') as file:
        file.write(tac_json)