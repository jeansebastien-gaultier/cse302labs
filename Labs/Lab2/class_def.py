class Statement:
    def __init__(self):
        return

class StatementVarDecl(Statement):
    def __init__(self, name,  linenolineno, type = "<type:int>", init = 0):
        self.name = name
        self.type = type
        self.init = init
        self.lineno = self.lineno

class StatementAssign(Statement):
    def __init__(self, target, expr, lineno):
        self.target = target
        self.expr = expr
        self.lineno = lineno

class StatementCall(Statement):
    def __init__(self, func, arguments, lineno):
        self.func = func
        self.arguments = arguments
        self.lineno = lineno


class Expression:
    def __init__(self):
        return

class ExpressionVar(Expression):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

class ExpressionInt(Expression):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno

class ExpressionUniOp(Expression):
    def __init__(self, operator, argument, lineno):
        self.operator = operator
        self.argument = argument
        self.lineno = lineno

class ExpressionBinOp(Expression):
    def __init__(self, argument_l, operator, argument_r, lineno):
        self.argument_l = argument_l
        self.operator = operator
        self.argument_r = argument_r
        self.lineno = lineno


def json_to_expr(js_obj):
    js_obj = js_obj[0]
    if js_obj[0] == '<expression:var>':
        return ExpressionVar(js_obj[1])

    elif js_obj[0] == '<expression:int>':
        return ExpressionInt(js_obj[1])

    elif js_obj[0] == '<unop>':
        operator = js_obj[1][0][0]
        argument = json_to_expr(js_obj[2]) 
        return ExpressionUniOp(operator, argument)

    elif js_obj[0] == '<binop>':
        left = json_to_expr(js_obj[1])
        operator = js_obj[2][0][0]
        right = json_to_expr(js_obj[3])
        return ExpressionBinOp(argument_l=left, operator=operator, argument_r=right)

    else:
        raise ValueError(f'Unrecognized <expression>: {js_obj}')


def json_to_statment(js_obj):
    js_obj = js_obj[0]
    if js_obj[0] == "<statement:vardecl>":
        name = js_obj[1][0]
        expr = json_to_expr(js_obj=js_obj[2])
        target_type = js_obj[3][0]
        return StatementVarDecl(name=name, init=expr, type=target_type)

    elif js_obj[0] == "<statement:assign>":
        target = json_to_expr(js_obj[1])
        expression = json_to_expr(js_obj[2])
        return StatementAssign(target=target, expr=expression)

    elif js_obj[0] == "<statement:eval>" and js_obj[1][0][0] == "<statement:call>":
        func = js_obj[1][0][1][0]
        arguments = [json_to_expr(js_obj[1][0][2][0])]
        return StatementCall(func=func, arguments=arguments)

    else:
        raise ValueError(f'This <statement> is not recognized: {js_obj}')