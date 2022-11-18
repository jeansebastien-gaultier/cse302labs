import sys, getopt, tac, cfg, ssagen, json

instructions = ['div', 'mod', 'call']   

def dead_store_elimination(CFG, flag = False, livein = {}, liveout = {}):
    cfg.recompute_liveness(CFG, livein, liveout)
    for _, blk in CFG._blockmap.items():
        size = len(blk.body)
        for ele in blk.body:
            if ele.opcode in instructions:
                continue
            if ele.dest == None or tac.Instr._istemp(ele.dest) == False or ele.dest in liveout[ele]:
                continue
            flag = True
    return flag


def copy_propagation(CFG):
    for _, blk in CFG._blockmap.items():
        for ele in blk.body:
            if ele == 'copy':
                arg1 = ele.arg1
                dest = ele.dest
                if tac.Instr._istemp(dest) == False or tac.Instr._istemp(arg1) == False:
                    continue
                for _, blk1 in CFG._blockmap.items():
                    for i in blk1.instrs():
                        if i.opcode == 'copy' or i.arg1 == None or i.arg2 == None:
                            continue
                        if i.arg1 == dest:
                            i.arg1 = arg1
                        if i.arg2 == dest:
                            i.arg2 = arg1
                        if i.opcode == 'phi':
                            for k,v in i.arg1.items():
                                if i.arg1[k] == dest:
                                    i.arg1[k] = arg1
            
def execute(tac_file):
    gvars, procs = dict(), dict()
    for decl in tac.load_tac(tac_file):
        if isinstance(decl, tac.Gvar): 
            gvars[decl.name] = decl
        else: 
            CFG = cfg.infer(decl)
            ssagen.crude_ssagen(decl, CFG)
            copy_propagation(CFG)
            dse = True
            while dse:
               dse = dead_store_elimination(CFG)

            cfg.linearize(decl, CFG)
            procs[decl.name] = CFG

            print(decl)

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], '-o', [])

    tac_file = args[0]

    execute(tac_file)

