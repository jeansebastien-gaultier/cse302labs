import sys
scopes = []

class Statment:
    def __init__(self):
        return


class StatementBlock(Statment):
    def __init__(self, body, lineno, col):
        self.body = body
        self.lineno = lineno
        self.col = col

    def type_check(self):
        scopes.append(dict())
        blk_ret = False
        for stmt in self.body:
            if not isinstance(stmt, Statment):
                for st in stmt:
                    blk_ret = max(st.type_check(), blk_ret)
            else:
                blk_ret = max(st.type_check(), blk_ret)
        scopes.pop()

        return blk_ret


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
        if self.type == 'void':
            print(f'File "_", line {self.initial.lineno}')
            print(f'Error: Variable "{self.name}" initialized with expression of different type "{self.initial.type}"')
            sys.exit(1)

        if self.initial.type != "void":
            print(f'File "_", line {self.initial.lineno}')
            print(f'Error: Variable "{self.name}" initialized with expression of different type "{self.initial.type}"')
            sys.exit(1)

        if self.intial.type != self.type:
            print(f'File "_", line {self.initial.lineno}')
            print(f'Error: Variable "{self.name}" initialized with expression of different type "{self.initial.type}"')
            sys.exit(1) 

        scopes[-1][self.name] = (self.initial.type, self.lineno)
        return False

    def to_tac(self):
        return {"var": self.name, "init": self.initial}


class StatementAssign(Statment):
    def __init__(self, target, expr, lineno, col):
        self.target = target
        self.expr = expr
        self.lineno = lineno
        self.col = col

    def type_check(self):
        self.target.type_check()
        self.expr.type_check()
        self.type = self.target.type

        if self.expr.type == 'void':
            print(f'File "_", line {self.arg.lineno}')
            print(f'Error: UNexpected declaratiom')
            sys.exit(1)

        if self.type != self.expr.type:
            print(f'File "_", line {self.arg.lineno}')
            print(f'Error: Unexpected expression')
            sys.exit(1)

        return False


class StatementCall(Statment):
    def __init__(self, function, args, lineno, col):
        self.function = function
        self.args = args
        self.lineno = lineno
        self.col = col

    def type_check(self):
        self.args[0].type_check()

class StaementEval(Statment):
    def __init__(self, expr, lineno, col):
        self.expr = expr
        self.lineno = lineno
        self.col = col

    def type_check(self):
        self.expr.type_check()
        self.type = self.expr.type
        return False


class StatementWhile(Statment):
    def __init__(self, condition, instructions, lineno, col):
        self.condition = condition
        self.instructions = instructions
        self.lineno = lineno
        self.col = col

    def type_check(self):
        self.condition.type_check()
        if self.condition.type != 'bool':
            print(f'File "_", line {self.arg.lineno}')
            print(f'Error: INvalid condition type')
            sys.exit(1)
        self.instructions.type_check()
        return False


class StatementIf(Statment):
    def __init__(self, condition, instructions, else_case, lineno):
        self.condition = condition
        self.instructions = instructions
        self.else_case = else_case
        self.lineno = lineno

    def type_check(self):
        self.condition.type_check()
        if self.condition.type != 'bool':
            print(f'File "_", line {self.arg.lineno}')
            print(f'Error: INvalid condition type')
            sys.exit(1)
        
        inst_t = self.instructions.type_check()
        inst_w = False
        if self.else_case is not None:
            inst_w = self.else_case.type_check()
        return inst_t and inst_w


class StructuredJump(Statment):
    def __init__(self, jump_type, lineno, col):
        self.jump_type = jump_type
        self.lineno = lineno
        self.col = col

    def type_check(self):
        return

class StatementReturn(Statment):
    def __init__(self, expr, lineno, col):
        self.expr = expr
        self.lineno = lineno
        self.col = col

    def type_check(self):
        if self.expr is not None:
            self.expr.type_check()
            self.type = self.expr.type

            if self.expr.type != scopes[1]:
                print(f'File "_", line {self.arg.lineno}')
                print(f'Error: INvalid return')
                sys.exit(1)
        else:
            self.type = "void"
            if scopes[1] != 'void':
                print(f'File "_", line {self.arg.lineno}')
                print(f'Error: INvalid return')
                sys.exit(1)
        return True


class Expression:
    def __init__(self):
        return


class ExpressionVar(Expression):
    def __init__(self, name, lineno, type, col):
        self.name = name
        self.lineno = lineno
        self.type = type
        self.col = col

    def type_check(self):
        for scope in reversed(scopes):
            if self.name in scope:
                if self.scope is None:
                    self.type = scope[self.name][0]
                elif self.scope != scope[self.name][0]:
                    print(f'File "_", line {self.arg.lineno}')
                    print(f'Error: Invalid type')
                    sys.exit(1)
                return
        else:
            print(f'File "_", line {self.lineno}')
            print(f'Error: Undeclared variable "{self.name}"')
            sys.exit(1)


class ExpressionInt(Expression):
    def __init__(self, value, lineno, col):
        self.value = value
        self.lineno = lineno
        self.type = 'int'
        self.col = col

    def type_check(self):
        return


class ExpressionBool(Expression):
    def __init__(self, value, lineno, col):
        self.value = value
        self.lineno = lineno
        self.type = 'bool'
        self.col = col

    def type_check(self):
        return


class ExpressionUniOp(Expression):
    def __init__(self, op, arg, lineno):
        self.op = op
        self.arg = arg
        self.lineno = lineno

    def type_check(self):
        self.arg.type_check()
        if self.op in ['not', 'sub', 'neg']:
            if self.arg.type == 'int':
                self.type = 'int'
            else:
                print(f'File "_", line {self.arg.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)
        
        elif self.op == 'NOT':
            if self.arg.type == 'bool':
                self.type = 'bool'
            else:
                print(f'File "_", line {self.arg.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)

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

        elif self.op in ['bor', 'band']:
            if self.arg_left.type == 'bool' and self.arg_right.type == 'bool':
                self.type = 'bool'
            else:
                print(f'File "_", line {self.arg_right.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)

        elif self.op in ['jz', 'jnz']:
            if (self.arg_left.type == 'bool' and self.arg_right.type == 'bool') or (self.arg_left.type == 'int' and self.arg_right.type == 'int'):
                self.type = 'bool'
            else:
                print(f'File "_", line {self.arg_right.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)
        elif self.op in ['jl', 'jnle',
                         'jle', 'jnl']:
            if self.arg_left.type == 'int' and self.arg_right.type == 'int':
                self.type = 'bool'
            else:
                print(f'File "_", line {self.arg_right.lineno}')
                print(f'Error: Operation and argumet type not comatible')
                sys.exit(1)
        else:
            print(f'File "_", line {self.arg_right.lineno}')
            print(f'Error: Unknown operation "{self.op}"')
            sys.exit(1)


class ProcDec:
    def __init__(self, name, args, type, body, lineno, col):

        if name.startswith('__bx_'):
            print(f'File "_", line {self.arg_right.lineno}')
            print(f'Error: Invalid name')
            sys.exit(1)

        self.name = name
        self.args = args
        self.type = type
        self.body = body
        self.lineno = lineno
        self.col = col

    def type_check(self):
        scopes.append(self.type)
        scopes.append(dict())

        for arg in self.args:
            if arg.name in scopes[-1]:
                print(f'File "_", line {self.arg_right.lineno}')
                print(f'Error: Argument already declared')
                sys.exit(1)
            else:
                scopes[-1][arg.name] = (arg.type, arg.lineno)

        proc_ret = self.body.type_check()
        scopes.pop()
        scopes.pop()

        if self.type != 'void' and not proc_ret:
            print(f'File "_", line {self.arg_right.lineno}')
            print(f'Error: Mising return')
            sys.exit(1)

    def to_tac(self):
        result = {"proc": self.name, "args": list(self.args), "body": []}
        for i in self.body:
            result["body"].append(i.to_tac())
        return result