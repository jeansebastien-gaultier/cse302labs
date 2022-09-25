"""
Jean-Sebastien Gaultier
LAB1 CSE302

Transform AST to TAC
"""


import json
import sys
import os

fresh_temporary = 0
VAR = {}
BINOP = {"addition": "add", "substraction": "sub", "multiplication": "mul", "division": "div", "modulus":"mod",
"bitwise-xor": "xor", "bitwise-or": "or", "bitwise-and":"and"}
UNOP = {"opposite": "not", "bitwise-negation": "neg"}

class Expression:
    def __init__(self):
        return

class ExpressionVar(Expression):
    def __init__(self, name):
        self.name = name

class ExpressionInt(Expression):
    def __init__(self, value):
        self.value = value

class ExpressionUniOp(Expression):
    def __init__(self, operator, argument):
        self.operator = operator
        self.argument = argument

class ExpressionBinOp(Expression):
    def __init__(self, argument_l, operator, argument_r):
        self.argument_l = argument_l
        self.operator = operator
        self.argument_r = argument_r

def json_to_name(js_obj):
    return js_obj[1]['value']

def json_to_expr(js_obj):
    if js_obj[0] == '<expression:var>':
        return ExpressionVar(json_to_name(js_obj[1]['name']))

    if js_obj[0] == '<expression:int>':
        return ExpressionInt(js_obj[1]['value'])

    if js_obj[0] == '<expression:uniop>':
        operator = json_to_name(js_obj[1]['operator'][1]['value'])
        argument = json_to_expr(js_obj[1]['argument'][0])
        return ExpressionUniOp(operator, argument)

    if js_obj[0] == '<expression:binop>':
        operator = json_to_name(js_obj[1]['operator'][1]['value'])
        argument_l = json_to_expr(js_obj[1]['left'])
        argument_r = json_to_expr(js_obj[1]['right']) 
        return ExpressionBinOp(argument_l, operator, argument_r)

    raise ValueError(f'Unrecognized <expression>: {js_obj[0]}')


class Statement:
    def __init__(self):
        return

class StatementVarDecl(Statement):
    def __init__(self, name, type = "<type:int>", init = 0):
        self.name = name
        self.type = type
        self.init = init

class StatementAssign(Statement):
    def __init__(self, l_value, r_value):
        self.l_value = l_value
        self.r_value = r_value

class StatementEval(Statement):
    def __init__(self, position, target, arguments):
        self.position = position
        self.target = target
        self.arguments = arguments

def json_to_statement(js_obj):
    if js_obj[0] == "<statement:vardecl>":
        name = js_obj[1]['name'][1]['value']
        type = js_obj[1]['type'][0]
        init = js_obj[1]['init'][1]['value']
        return StatementVarDecl(name, type, init)
    
    if js_obj[0] == "<statement:assign>":
        l_value = js_obj[1]['l_value']
        r_value = json_to_expr(js_obj[1]['r_value'])
        return StatementAssign(l_value, r_value)

    if js_obj[0] == "<statement:eval>" and js_obj[1]['expression'][0] == "<expression:call>":
        position = js_obj[1]['position']
        target = js_obj[1]['expression'][1]['target'][1]['value']
        arguments = json_to_expr(js_obj[1]['expression'][1]['arguments'][0])
        return StatementEval(position, target, arguments)

    raise ValueError(f'Unrecognized <statement>: {js_obj[0]}')

def tmm_expr(expression, tac):
    global BINOP, UNOP, fresh_temporary, VAR

    if isinstance(expression, ExpressionInt):
        return "const", [expression.value]

    elif isinstance(expression, ExpressionVar):
        return "copy", [VAR[expression.name]]

    elif isinstance(expression, ExpressionBinOp):
        result1 = f'%{str(fresh_temporary)}'
        fresh_temporary+=1
        op, argument = tmm_expr(expression.argument_l, tac)
        tac[0]["body"].append({"opcode": op, "args": argument, "result": result1})
        result2 = f'%{str(fresh_temporary)}'
        fresh_temporary+=1
        op, argument = tmm_expr(expression.argument_r, tac)
        tac[0]["body"].append({"opcode": op, "args": argument, "result": result2})
        return BINOP[expression.op], [result1, result2]

    elif isinstance(expression, ExpressionUniOp):
        result = f'%{str(fresh_temporary)}'
        fresh_temporary+=1
        operator, argument = tmm_expr(expression.argument, tac)
        tac[0]['body'].append({"opcode": op, "args": argument, "result":result})
        return UNOP[expression.op], [result]
    
    else:
        return "EXpression not recognized"



    # if expression[0] == '<expression:var>':
    #     instruction = [{'opcode': 'const', 'args': [expression[1]], 'result': f'%{fresh_temporary}'}]

    # elif expression[0] == '<expression:int>':
    #     return

    # elif expression[0] == '<expression:uniop>':
    #     return

    # elif expression[0] == '<expression:binop>':
    #     return 

def tmm_statements(instructions, tac):
    global fresh_temporary, VAR

    for inst in instructions:
        if isinstance(inst, StatementVarDecl):
            result = f'%{fresh_temporary}'
            fresh_temporary+=1
            operator, argument = tmm_expr(inst.init, tac)
            tac[0]['body'].append({"opcode":operator, "args":argument, "result":result})
            
        elif isinstance(inst, StatementAssign):
            result = VAR[inst.target.name]
            op, argument = tmm_expr (inst.expr, tac)
            tac[0]['body'].append({'opcode':operator, "args":argument, "result":result})
            
        elif isinstance(inst, StatementEval):
            result = f'%{fresh_temporary}'
            fresh_temporary+=1
            op, argument = tmm_expr(inst.argument[0], tac)
            tac[0]['body'].append({"opcode":operator, "args":argument, "result":result})
            tac[0]['body'].append({'opcode':inst.target, "args": [result], "result": null})
    
        else:
            return "Instruction not recognized"



def main():
    ast_file = sys.argv[1]
    if not ast_file.endswith('.json'):
        return ('Please provide a .json file and not something else')

    with open(ast_file, 'r') as fp:
        js_obj = json.load(fp)

    ast = js_obj['ast'][0]
    statements = js_obj['ast'][0][0]
    tac = [ { "proc": "@main", "body": [] } ]
    inst = [json_to_statement(statement) for statement in statements]
    tmm_statements(inst, tac)

    with open(ast_file[:-5] + '.tac.json', 'w') as file:
        file.write(json.dump(tac, file))

if __name__ == "__main__":
    main()


