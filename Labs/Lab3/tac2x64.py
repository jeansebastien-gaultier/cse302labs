import json
import sys
import getopt


class Instr:
    def __init__(self, opcode, arg1, arg2, dest):
        self.opcode = opcode
        self.arg1 = arg1
        self.arg2 = arg2
        self.dest = dest


class Create_x64:
    def __init__(self):
        self.stack = {}
        self.strs = []
        self.stackp = 0
        self.binop = {'add': 'addq', 'sub': 'subq', 'mul': 'imulq',
                      'and': 'andq', 'or': 'orq', 'xor': 'xorq'}
        self.unop = {'not': 'notq', 'neg': 'negq'}
        self.shiftop = {'shl': 'salq', 'shr': 'sarq'}
        self.div = {'div': '%rax', 'mod': '%rdx'}
        self.condition = ['je', 'jz', 'jne', 'jnz', 'jl',
                          'jnge', 'jle', 'jng', 'jg', 'jnle', 'jge', 'jnl']

    def get_pos(self, var):
        if var in self.stack.keys():
            return self.stack[var]
        else:
            self.stackp += 1
            self.stack[var] = self.stackp
            return self.stackp

    def to_str(self, tac_expr):
        op = tac_expr.opcode
        dest = tac_expr.dest
        arg1 = tac_expr.arg1
        arg2 = tac_expr.arg2

        if op == 'const':
            self.strs.append("\tmovabsq ${}, %rax".format(arg1))
            self.strs.append("\tmovq %rax, {}(%rbp)".format(-8 * self.get_pos(dest)))

        elif op == 'copy':
            self.strs.append("\tmovq {}(%rbp), %r8".format(-8 * self.get_pos(arg1)))
            self.strs.append("\tmovq %r8, {}(%rbp)".format(-8 * self.get_pos(dest)))

        elif op == 'print':
            self.strs.append("\tmovq {}(%rbp), %rdi".format(-8 * self.get_pos(arg1)))
            self.strs.append("\tcallq bx_print_int")

        elif op == 'label':
            self.strs.append(".main{}:".format(arg1[1:]))

        elif op == 'jmp':
            self.strs.append("\tjmp .main{}".format(arg1[1:]))

        elif op in self.binop.keys():
            self.strs.append("\tmovq {}(%rbp), %r8".format(-8 * self.get_pos(arg1)))
            self.strs.append("\t{} {}(%rbp), %r8".format(self.binop[op], -8 * self.get_pos(arg2)))
            self.strs.append("\tmovq %r8, {}(%rbp)".format(-8 * self.get_pos(dest)))

        elif op in self.unop.keys():
            self.strs.append("\tmovq {}(%rbp), %r8".format(-8 * self.get_pos(arg1)))
            self.strs.append("\t{} %r8".format(self.unop[op]))
            self.strs.append("\tmovq %r8, {}(%rbp)".format(-8 * self.get_pos(dest)))

        elif op in self.shiftop.keys():
            self.strs.append("\tmovq {}(%rbp), %r8".format(-8 * self.get_pos(arg1)))
            self.strs.append("\tmovq {}(%rbp), %rcx".format(-8 * self.get_pos(arg2)))
            self.strs.append("\t{} %cl, %r8".format(self.shiftop[op]))
            self.strs.append("\tmovq %r8, {}(%rbp)".format(-8 * self.get_pos(dest)))

        elif op in self.div.keys():
            self.strs.append("\tmovq {}(%rbp), %rax".format(-8 * self.get_pos(arg1)))
            self.strs.append("\tcqto".format())
            self.strs.append("\tidivq {}(%rbp)".format(-8 * self.get_pos(arg2)))
            self.strs.append("\tmovq {}, {}(%rbp)".format(self.div[op], -8 * self.get_pos(dest)))

        elif op in self.condition:
            self.strs.append("\tmovq {}(%rbp),%rax".format(-8 * self.get_pos(arg1)))
            self.strs.append("\tcmpq $0, %rax".format())
            self.strs.append("\t{} {}".format(op, arg2[1:]))

    def main(self, tac_file):
        for line in tac_file:
            self.to_str(line)
        head = ['\t.text', '\t.globl main', 'main:', '\tpushq %rbp',
                '\tmovq %rsp, %rbp', "\tsubq ${}, %rsp".format(8 * len(self.stack))]
        tail = ['\tmovq %rbp, %rsp ', '\tpopq %rbp ',
                '\txorl %eax, %eax', '\tretq']
        return head + self.strs + tail


def tac2x64(file):   
    with open(file, 'r') as fp:
        ufp = json.load(fp)
        tac = []
        for line in ufp[0]["body"]:
            if (len(line["args"]) >= 1):
                arg1 = line["args"][0]
                if (len(line["args"]) == 2):
                    arg2 = line["args"][1]
                else:
                    arg2 = None
            else:
                arg1, arg2 = None, None
            tac.append(Instr(line["opcode"], arg1, arg2, line["result"]))

    outfile = Create_x64()
    out = outfile.main(tac)
    return out