import sys, getopt, json

from json_to_stat import ProcDec, StatementVarDecl
from tac2x64 import Instr

conditional_jumps = {'jz', 'jnz', 'jl', 'jle', 'jnl', 'jnle'}

conditional_jumps_pars = {'je': ['je', 'jle', 'jge'], 'jne': ['jne'], 'jl': ['jl', 'jne', 'jle'], 'jle': ['jle'], 'jg': ['jg', 'jne', 'jge'], 'jge': ['jge']}

class Inst:
    def __init__(self, instruction):
        self.instruction = instruction
        self.id = id(instruction)
        self.child = []

    def check(self, tmp):
        return (tmp != None) and (isinstance(tmp, str)) and (tmp[0] == '%')

    def __str__(self):
        return f'opcode : {self.instruction.opcode}, arg : {[self.instruction.arg1, self.instruction.arg2]}, dest : {self.instruction.dest}'


class Block:
    def __init__(self, instructions):
        self.label = instructions[0].instruction.arg1
        self.instructions = instructions
        self.child = []
        self.father = []

    def add_father(self, father):
        self.father.append(father)

    def add_child(self, child):
        self.child.append(child)

    def union(self, tmp):
        self.instructions += tmp.instructions
        for child_label in tmp.child:
            self.child.append(child_label)


class CFG:
    def __init__(self, tac_file, proc_name):
        self.name = proc_name[1:]
        self.build(tac_file)

    def build(self, tac_file):
        self.block = {}
        self.instructions = {}
        self.tac_id = []

        count = 0
        i = 0
        if tac_file[0].opcode == 'label':
            self.entry_label = tac_file[0].arg1
        else:
            tac_file.insert(0, Instr('label', f'.Lentry {self.name}', None, None))
            self.entry_label = f'.Lentry {self.name}'

        tac_len = len(tac_file)
        while i < tac_len:
            if i < tac_len -1:
                succ = tac_file[i+1]
            if tac_file[i].opcode == 'jmp':
                if i < tac_len -1:
                    if succ.opcode != 'label':
                        count +=1
                        tac_file.insert(i +1, Instr('label', f'.Ljmp_{self.name}_{count}', None, None))
            elif i>=1:
                if tac_file[i] == 'label':
                    if tac_file[i-1].opcode != 'jmp':
                        if tac_file[i-1].opcode == 'ret':
                            tac_file.insert(i, Instr('jmp', tac_file[i].arg1, None, 'tmp'))
                        else:
                            tac_file.insert(i, Instr('jmp', tac_file[i].arg1, None, None))

            tmp = Inst(tac_file[i])
            self.instructions[tmp.id] = tmp
            self.tac_id.append(tmp.id)
            i += 1

        self.block[tac_file[0].arg1] = Block([self.instructions[self.tac_id[0]]])
        prev = tac_file[0].arg1

        edge = []

        for i in range(1, tac_len):
            id_tac = self.tac_id[i]
            if tac_file[i].opcode == 'label':
                self.block[tac_file[i].arg1] = Block ([self.instructions[id_tac]])
                prev = tac_file[i].arg1
            else:
                self.block[prev].instructions.append(self.instructions[id_tac])

            if tac_file[i].opcode in conditional_jumps:
                edge.append((prev, tac_file[i].arg2))

            if tac_file[i].opcode == 'jmp':
                edge.append((prev, tac_file[i].arg1))

        for i in range(1, tac_len):
            id_tac = self.tac_id[i]

            if tac_file[i].opcode in conditional_jumps:
                if (len(self.block[tac_file[i].arg2].instructions) > 1):
                    self.instructions[id_tac].child.append(self.block[tac_file[i].arg2].instructions[1].id)
            if tac_file[i].opcode == 'jmp':
                if (len(self.block[tac_file[i].arg1].instructions) > 1):
                    self.instructions[id_tac].child.append(self.block[tac_file[i].arg1].instructions[1].id)
                continue

            if i < tac_len - 1:
                if (self.instructions[self.tac_id[i + 1]].instruction.opcode != 'label'):
                    self.instructions[id_tac].child.append(self.tac_id[i + 1])

        for (f, c) in edge:
            self.block[f].add_child(c)
            self.block[c].add_father(f)


    def jump_thread(self):

        def visited(current, past):
            if len(current.child) == 1:
                c_label = list(current.child)[0]
                if len(self.block[c_label].father) ==1:
                    past +=[c_label]
                    return visited(self.block[c_label], past)
            return past

        NNB = set()

        for lab, blk in self.block.items():
            past = visited(blk, [lab])[:-1]
            past_len = len(past)
            if past_len >1:
                tr = True
                for i in range(1, past_len -1):
                    if len(past[i]) >2:
                        tr = False
                        break
                
                if tr:
                    head = self.block[past[0]]
                    head.instructions[-1].instruction.arg1 = past[-1]
                    for i in past[-1]:
                        head.union(self.block[i])
                        NNB.add(i)

            for c_label in blk.child:
                variable = None
                jmp = None
                for inst in blk.instructions:
                    if inst.instruction.arg2 == c_label:
                        if inst.instruction.opcode in conditional_jumps:
                            variable = inst.instruction.arg1
                            jmp = inst.instruction.opcode

                tr = False
                child = self.block[c_label]
                for inst in child.instructions:
                    if inst.instruction.dest == variable:
                        tr = True
                        break

                tr = False
                for i in range(len(child.instructions) - 1):
                    if len(child.father) != 1:
                        break
                    if child.instructions[i].instruction.opcode == jmp:
                        if child.instructions[i].instruction.arg1 == variable:
                            child.instructions[i].instruction.opcode = 'nop'
                            if child.instructions[i + 1].instruction.opcode == 'jmp':
                                child.instructions[i + 1].instruction.arg1 = child.instructions[i].instruction.arg2
                            tr = True
            
        for i in NNB:
            self.block.pop(i,None)
            self.remove(i)


    def clean(self, Bool = True):
        all_labels = self.block[self.entry_label]
        past = list(all_labels.instructions)
        past_label = set([self.entry_label])

        def new_visited(current):
            if current.instructions[-1].instruction.opcode == 'jmp':
                if current.instructions[-1].instruction.arg1 not in past_label:
                    # child = self.block[current.instructions[-1].instruction.arg1]
                    past_label.add(current.instructions[-1].instruction.arg1)
                    if self.block[current.instructions[-1].instruction.arg1].instructions[-1].instruction.opcode != 'jmp':
                        if self.block[current.instructions[-1].instruction.arg1].instructions[-1].instruction.opcode != 'ret':
                            self.block[current.instructions[-1].instruction.arg1].instructions += [Inst(Instr('ret', None, None, None))]
                    past.extend(self.block[current.instructions[-1].instruction.arg1].instructions)
                    new_visited(self.block[current.instructions[-1].instruction.arg1])
            for child_label in current.child:
                if child_label in past_label:
                    continue
                child = self.block[child_label]
                past_label.add(child_label)
                if (child.instructions[-1].instruction.opcode != 'jmp'):
                    if (child.instructions[-1].instruction.opcode != 'ret'):
                        child.instructions += [Inst(Instr('ret', None, None, None))]
                past.extend(child.instructions)
                new_visited(child)

        new_visited(all_labels)
        
        for lab in past:
            if (lab.instruction.opcode == 'jmp'):
                if lab.instruction.dest == 'tmp':
                    lab.instruction.opcode = 'nop'
                    continue

            if lab.instruction.opcode != 'label':
                continue

            label = lab.instruction.arg1
            f = False

            for i in past:
                if i.instruction.opcode in conditional_jumps:
                    if (label == i.instruction.arg2):
                        f = True
                        break

                elif i.instruction.opcode == 'jmp':
                    if label == i.instruction.arg1:
                        f = True
                        break

            if not f:
                lab.instruction.opcode = 'nop'

        if Bool:
            tac = []
            size_tac = len(tac)
            count = 0
            for i in past:
                tac.append(i.instruction)

            for i in range(size_tac - 1):
                current= tac[i - count]
                if current.opcode == 'jmp':
                    succ = tac[i-count + 1]

                    if (succ.opcode == 'label'):
                        if succ.arg1 == current.arg1:
                            tac.pop(i-count)
                            count += 1

            count = 0
            for i in range(size_tac - 1):
                current = tac[i- count]
                if current.opcode == 'ret':
                    if current.arg1 == None:
                        succ = tac[i-count + 1]
                        if (succ.opcode == 'ret'):
                            tac.pop(i - count)
                            count += 1
                    else:
                        succ = tac[i - count + 1]
                        if (succ.opcode == 'ret'):
                            tac.pop(i - count + 1)
                            count += 1
        else:
            tac = [i.instruction for i in past]

        return list(filter(lambda instr: instr.opcode != 'nop', tac))


    def modify_blocks(self):
        for blk in self.block.values():
            if len(blk.child) == 1:
                c_label = list(blk.child)[0]
                child = self.block[list(blk.child)[0]]
                if (len(child.father) != 1):
                    continue
                if (c_label == self.entry_label):
                    continue
                if blk.instructions[-1].instruction.opcode == 'jmp':
                    blk.instructions[-1].instruction.opcode = 'nop'
                    blk.union(child)
                    self.block.pop(list(blk.child)[0])
                    #self.remove(c_label)
                    for block in self.block.values():
                        if c_label in block.child:
                            block.child.remove(c_label)
                        if c_label in block.father:
                            block.father.remove(c_label)
                    return blk.label , c_label
        return False

    def optimization(self):
        self.jump_thread()
        self.build(self.clean(False))
        merged = set()
        while True:
            current = self.modify_blocks()
            self.build(self.clean(False))
            if current == True:
                if current not in merged:
                    merged.add(current)
                else:
                    break
            else:
                break      

def final(filename):
    with open(filename, 'r') as fp:
        js_obj = json.load(fp)
        res = []
        for current in js_obj:
            if 'proc' in current.keys():
                tac = []
                for line in current['body']:
                    op, dest = line['opcode'], line['result']
                    arg1, arg2 = None, None
                    if len(line['args']) == 1:
                        arg1 = line['args'][0]
                    elif len(line['args']) ==2:
                        arg1 = line['args'][0]
                        arg2 = line['args'][1]
                    tac.append(Instr(op, arg1, arg2, dest))
                res.append(ProcDec(current['proc'], current['args'], None, tac, None, None))
            elif 'var' in current:
                res.append(StatementVarDecl(current['var'], current['ini'], None, None, None))

    process = []
    variables = []
    for decl in res:
        if isinstance(decl, ProcDec):
            if decl.body == []:
                process.append(ProcDec(decl.name, decl.args,
                             None, decl.body, None, None))
                continue
            cfg = CFG(decl.body, decl.name)
            cfg.optimization()
            proc_instrs = cfg.clean()
            process.append(ProcDec(decl.name, decl.args,
                         None, proc_instrs, None, None))
        elif isinstance(decl, StatementVarDecl):
            variables.append(decl)



if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    final(args[0])