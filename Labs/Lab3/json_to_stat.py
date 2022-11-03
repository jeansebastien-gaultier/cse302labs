import sys
scopes = []

class Statment:
    pass


class StatementBlock(Statment):
    def __init__(self, body):
        self.body = body

    def type_check(self):
        scopes.append(dict())
        for stmt in self.body:
            stmt.type_check()
        scopes.pop()


class StatementVarDecl(Statment):
    def __init__(self, name, initial, type, lineno):
        self.name = name
        self.initial = initial
        self.type = type
        self.lineno = lineno

    def type_check(self):
        if self.name in scopes[-1]:
            print(f'File "_", line {self.lineno}')
            print(f'Error: Redeclared variable "{self.name}"')
            sys.exit(1)

        self.initial.type_check()
        if self.initial.type != self.type:
            print(f'File "_", line {self.initial.lineno}')
            print(f'Error: Variable "{self.name}" initialized with expression of different type "{self.initial.type}"')
            sys.exit(1)

        scopes[-1][self.name] = (self.initial.type, self.lineno)


class StatementAssign(Statment):
    def __init__(self, target, expr, lineno):
        self.target = target
        self.expr = expr
        self.lineno = lineno

    def type_check(self):
        self.target.type_check()
        self.expr.type_check()
        self.type = self.target.type


class StatementCall(Statment):
    def __init__(self, function, args, lineno):
        self.function = function
        self.args = args
        self.lineno = lineno

    def type_check(self):
        self.args[0].type_check()


class StatementWhile(Statment):
    def __init__(self, condition, instructions, lineno):
        self.condition = condition
        self.instructions = instructions
        self.lineno = lineno

    def type_check(self):
        self.condition.type_check()
        self.instructions.type_check()


class StatementIf(Statment):
    def __init__(self, condition, instructions, else_case, lineno):
        self.condition = condition
        self.instructions = instructions
        self.else_case = else_case
        self.lineno = lineno

    def type_check(self):
        self.condition.type_check()
        self.instructions.type_check()
        if self.else_case is not None:
            self.else_case.type_check()


class StructuredJump(Statment):
    def __init__(self, jump_type, lineno):
        self.jump_type = jump_type
        self.lineno = lineno

    def type_check(self):
        return


class Expression:
    pass


class ExpressionVar(Expression):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def type_check(self):
        for scope in reversed(scopes):
            if self.name in scope:
                self.type = scope[self.name][0]
                return
        else:
            print(f'File "_", line {self.lineno}')
            print(f'Error: Undeclared variable "{self.name}"')
            sys.exit(1)


class ExpressionInt(Expression):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno
        self.type = 'int'

    def type_check(self):
        return


class ExpressionBool(Expression):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno
        self.type = 'bool'

    def type_check(self):
        return


class ExpressionUniOp(Expression):
    def __init__(self, op, arg, lineno):
        self.op = op
        self.arg = arg
        self.lineno = lineno

    def type_check(self):
        self.arg.type_check()
        if self.op in ['not', 'sub', 'neg'] and self.arg.type == 'int':
            self.type = 'int'
        elif self.op == 'NOT':
            self.type = 'bool'
        else:
            print(f'File "_", line {self.arg.lineno}')
            print(f'Error: Operation and argumet type not comatible')
            sys.exit(1)


class ExpressionBinOp(Expression):
    def __init__(self, arg_left, op, arg_right, lineno):
        self.arg_left = arg_left
        self.arg_right = arg_right
        self.op = op
        self.lineno = lineno

    def type_check(self):
        self.arg_left.type_check()
        self.arg_right.type_check()
        if self.op in ['add', 'sub', 'mul', 'div', 'mod', 'shr',
                       'shl', 'xor', 'or', 'and']:
            if self.arg_left.type == 'int' and self.arg_right.type == 'int':
                self.type = 'int'
            else:
                print(f'File "_", line {self.arg_right.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)

        elif self.op in ['bor', 'band', 'jz', 'jnz', 'jl', 'jnle',
                         'jle', 'jnl']:
            self.type = 'bool'
        else:
            print(f'File "_", line {self.arg_right.lineno}')
            print(f'Error: Unknown operation "{self.op}"')
            sys.exit(1)