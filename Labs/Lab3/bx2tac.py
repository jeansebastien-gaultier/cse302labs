import json
import sys
import getopt
from json_to_stat import *
from myParser import Parser

filename = ''
next_temorary = 0
next_label = 0
__break_stack = []
__continue_stack = []


def eval_bool_exp(expression, tac):
    global next_temorary
    global next_label

    L1 = "%.L" + str(next_label)
    next_label += 1
    L2 = "%.L" + str(next_label)

    tac[0]['body'].append({'opcode': 'const', 'args': [0], 'result': '%' + str(next_temorary)})
    bool_exp(expression, L1, L2, tac)
    tac[0]['body'].append({'opcode': 'label', 'args': [L1], 'result': None})
    tac[0]['body'].append({'opcode': 'const', 'args': [1], 'result': '%' + str(next_temorary)})
    tac[0]['body'].append({'opcode': 'label', 'args': [L2], 'result': None})
    next_temorary += 1
    next_label += 1

    return (f'%{str(next_temorary)}')


def bool_exp(expression, Lt, Lf, tac):
    global next_temorary
    global next_label
    global filename

    if expression.type != 'bool':
        errorBx(filename, "UnexpExp", expression)

    if isinstance(expression, ExpressionBool):
        if expression.value == 'true':
            tac[0]['body'].append({"opcode": "jmp", "args": [Lt], "result": None})
        elif expression.value == 'false':
            tac[0]['body'].append({"opcode": "jmp", "args": [Lf], "result": None})
        else:
            errorBx(filename, "UnknVal", expression)

    elif isinstance(expression, ExpressionVar):
        for scope in reversed(scopes):
            if expression.name in scope:
                value = scope[expression.name][0]
                tac[0]['body'].append({'opcode': 'jz', 'args': [value, Lf], 'result': None})
                tac[0]['body'].append({'opcode': 'jmp', 'args': [Lt], 'result': None})
                
                return
        else:
            errorBx(filename, "UndcVar", expression)

    elif isinstance(expression, ExpressionUniOp):
        if expression.arg.type == 'bool':
            bool_exp(expression.arg, Lf, Lt, tac)
        elif expression.arg.type == 'int': 
            arg = '%' + str(next_temorary)
            next_temorary += 1

            op, args = expr_to_tac(expression.arg, tac)
            tac[0]["body"].append({"opcode": op, "args": args, "result": arg})

            tac[0]["body"].append({"opcode": 'jz', 'args': [arg, Lt], 'result': None})
            tac[0]['body'].append({"opcode": "jmp", 'args': [Lf], 'result': None})

        else:
            errorBx(filename, "UnexpExp", expression.arg)

    elif isinstance(expression, ExpressionBinOp):
        if expression.op in ['jz', 'jnz', 'jl', 'jle', 'jnle', 'jnl']:
            arg1 = '%' + str(next_temorary)
            next_temorary += 1

            if expression.arg_left.type == 'int':
                op, args = expr_to_tac(expression.arg_left, tac)
                tac[0]["body"].append({"opcode": op, "args": args, "result": arg1})

            elif expression.arg_left.type == 'bool':
                temp = eval_bool_exp(expression.arg_left, tac)
                tac[0]["body"].append({"opcode": 'copy', 'args': [temp], "result": arg1})
            else:
                errorBx(filename, "UnexpExp", expression.arg_left)

            arg2 = '%' + str(next_temorary)
            next_temorary += 1

            if expression.arg_right.type == 'int':
                op, args = expr_to_tac(expression.arg_right, tac)
                tac[0]["body"].append({"opcode": op, "args": args, "result": arg2})

            elif expression.arg_right.type == 'bool':
                temp = eval_bool_exp(expression.arg_right, tac)
                tac[0]["body"].append({"opcode": 'copy', 'args': [temp], "result": arg2})
            else:
                errorBx(filename, "UnexpExp", expression.arg_right)

            tac[0]["body"].append({'opcode': "sub", 'args': [arg1, arg2], "result": arg1})
            tac[0]["body"].append({"opcode": expression.op, 'args': [arg1, Lt], 'result': None})
            tac[0]['body'].append({"opcode": "jmp", 'args': [Lf], 'result': None})

        elif expression.op == 'band':
            Li = "%.L" + str(next_label)
            next_label += 1

            bool_exp(expression.arg_left, Li, Lf, tac)
            tac[0]['body'].append({"opcode": 'label',  'args': [Li], 'result': None})
            bool_exp(expression.arg_right, Lt, Lf, tac)

        elif expression.op == 'bor':
            Li = "%.L" + str(next_label)
            next_label += 1

            bool_exp(expression.arg_left, Lt, Li, tac)
            tac[0]['body'].append({"opcode": 'label',  'args': [Li], 'result': None})
            bool_exp(expression.arg_right, Lt, Lf, tac)

        else:
            errorBx(filename, "UnknOp", expression.arg_right, val2=expression)

    else:
        errorBx(filename, "UnknExpr", expression)


def expr_to_tac(expression, tac):
    global next_temorary
    global filename

    if expression.type != 'int':
        errorBx(filename, "UnexpExp", expression)

    if isinstance(expression, ExpressionInt):
        return "const", [expression.value]

    elif isinstance(expression, ExpressionVar):
        for scope in reversed(scopes):
            if expression.name in scope:
                return "copy", [scope[expression.name][0]]
        else:
            errorBx(filename, "UndcVar", expression)

    elif isinstance(expression, ExpressionUniOp):
        arg1 = '%' + str(next_temorary)
        next_temorary += 1

        op, args = expr_to_tac(expression.arg, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": arg1})

        return expression.op, [arg1]

    elif isinstance(expression, ExpressionBinOp):
        arg1 = '%' + str(next_temorary)
        next_temorary += 1

        op, args = expr_to_tac(expression.arg_left, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": arg1})

        arg2 = '%' + str(next_temorary)
        next_temorary += 1

        op, args = expr_to_tac(expression.arg_right, tac)
        tac[0]["body"].append({"opcode": op, "args": args, "result": arg2})

        return expression.op, [arg1, arg2]

    else:
        errorBx(filename, "UnknExpr", expression)


def statements_to_tac(instruction, tac):
    global next_temorary
    global next_label
    global filename

    if isinstance(instruction, StatementBlock):
        scopes.append(dict())
        for stmt in instruction.body:
            statements_to_tac(stmt, tac)
        scopes.pop()
    
    elif isinstance(instruction, StatementVarDecl):
        if instruction.name in scopes[-1]:
            errorBx(filename, "RedcVar", instruction)

        result = '%' + str(next_temorary)
        next_temorary += 1

        if instruction.type == 'int':
            if instruction.initial.type != 'int':
                errorBx(filename, "VarFail", instruction.initial, val2=instruction)

            op, args = expr_to_tac(instruction.initial, tac)
            tac[0]["body"].append({"opcode": op, "args": args, "result": result})

        elif instruction.type == 'bool':
            if instruction.initial.type != 'bool':
                errorBx(filename, "VarFail", instruction.initial, val2=instruction)

            temp = eval_bool_exp(instruction.initial, tac)
            tac[0]['body'].append({'opcode': 'copy', 'args': [temp], 'result': result})

        else:
            errorBx(filename, "VarFail", instruction, val2=instruction)

        scopes[-1][instruction.name] = (result, instruction.lineno)

    elif isinstance(instruction, StatementAssign):
        for scope in reversed(scopes):
            if instruction.target.name in scope:

                result = scope[instruction.target.name][0]
                
                if instruction.type == 'int':
                    if instruction.expr.type != 'int':
                        errorBx(filename, "VarFail", instruction.expr, val2=instruction.target)

                    op, args = expr_to_tac(instruction.expr, tac)
                    tac[0]["body"].append({"opcode": op, "args": args, "result": result})

                elif instruction.type == 'bool':
                    if instruction.expr.type != 'bool':
                        errorBx(filename, "VarFail", instruction.expr, val2=instruction.target)

                    temp = eval_bool_exp(instruction.expr, tac)
                    tac[0]['body'].append({'opcode': 'copy', 'args': [temp], 'result': result})

                else:
                    errorBx(filename, "VarFail", instruction, val2=instruction)

                return
        else:
            errorBx(filename, "UndcVar", instruction.target)

    elif isinstance(instruction, StatementCall):
        result = '%' + str(next_temorary)
        next_temorary += 1

        if instruction.args[0].type == 'int':
            op, args = expr_to_tac(instruction.args[0], tac)
            tac[0]["body"].append({"opcode": op, "args": args, "result": result})
        else:
            errorBx(filename, "PrintFail", instruction.args[0])

        tac[0]["body"].append({"opcode": instruction.function, "args": [result], "result": None})

    elif isinstance(instruction, StatementIf):
        Lt = "%.L" + str(next_label)
        next_label += 1
        Lf = "%.L" + str(next_label)
        next_label += 1

        bool_exp(instruction.condition, Lt, Lf, tac)
        tac[0]["body"].append({'opcode': 'label', 'args': [Lt], 'result': None})
        statements_to_tac(instruction.instructions, tac)

        if instruction.else_case is None:
            tac[0]["body"].append({'opcode': 'label', 'args': [Lf], 'result': None})
        else:
            Lo = "%.L" + str(next_label)
            next_label += 1
            tac[0]["body"].append({'opcode': 'jmp', 'args': [Lo], 'result': None})
            tac[0]["body"].append({'opcode': 'label', 'args': [Lf], 'result': None})
            statements_to_tac(instruction.else_case, tac)
            tac[0]["body"].append({'opcode': 'label', 'args': [Lo], 'result': None})

    elif isinstance(instruction, StatementWhile):
        Lhead = "%.L" + str(next_label)
        next_label += 1
        tac[0]["body"].append({'opcode': 'label', 'args': [Lhead], 'result': None})

        Lbod = "%.L" + str(next_label)
        next_label += 1
        Lend = "%.L" + str(next_label)
        next_label += 1

        __break_stack.append(Lend)
        __continue_stack.append(Lhead)
        bool_exp(instruction.condition, Lbod, Lend, tac)
        tac[0]["body"].append({'opcode': 'label', 'args': [Lbod], 'result': None})
        statements_to_tac(instruction.instructions, tac)
        tac[0]["body"].append({'opcode': 'jmp', 'args': [Lhead], 'result': None})
        tac[0]["body"].append({'opcode': 'label', 'args': [Lend], 'result': None})
        __continue_stack.pop()
        __break_stack.pop()

    elif isinstance(instruction, StructuredJump):
        if instruction.jump_type == 'break':
            if len(__break_stack) == 0:
                errorBx(filename, "InstFail", instruction)

            tac[0]['body'].append({'opcode': 'jmp', 'args': [__break_stack[-1]], 'result': None})

        elif instruction.jump_type == 'continue':
            if len(__continue_stack) == 0:
                errorBx(filename, "InstFail", instruction)

            tac[0]['body'].append({'opcode': 'jmp', 'args': [__continue_stack[-1]], 'result': None})

    else:
        errorBx(filename, "UnknStat", instruction)


def errorBx(filename, err, val1, val2=None):
    print(f'File "{filename}", line {val1.lineno}')
    if err == "UnexpExp":
        print(f'Error: Unexpected expression of type "{val1.type}"')
    elif err == "UnknExpr":
        print(f'Error: Unknown expression "{val1}"')
    elif err == "UnknStat":
        print(f'Error: Unknown statement "{val1}"')
    elif err == "VarFail":
        print(f'Error: Variable "{val2.name}" has wrong type')
    elif err == "PrintFail":
        print(f'Error: Unexpected type "{val1.type}" in print')
    elif err == "InstFail":
        print(f'Error: Misplaced instruction')
    elif err == "UndcVar":
        print(f'Error: Undeclared variable "{val1.name}"')
    elif err == "RedcVar":
        print(f'Error: Redeclared variable "{val1.name}"')
    elif err == "UnknOp":
        print(f'Error: Unknown operation "{val2.op}"')
    elif err == "UnknVal":
        print(f'Error: Unknown value "{val1.name}"')
    else:
        print("Error: Unknown Error")
    sys.exit(1)

def errorJ(filename, err, val1, val2=None):
    print(f'File "{filename}", line {val1.lineno}')
    if err == "RedcVar":
        print(f'Error: Redeclared variable "{val1.name}"')


def bx2tac(code, file):
    global filename
    filename = file
    parser = Parser(filename)

    try:
        statements = parser.parse(code)
    except SyntaxError as err:
        print('Syntax error:', err)
        sys.exit(1)

    tac = [{"proc": "@main", "body": []}]

    statements.type_check()
    statements_to_tac(statements, tac)
    return json.dumps(tac)