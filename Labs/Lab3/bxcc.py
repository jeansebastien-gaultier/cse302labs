from bx2tac import bx2tac
from tac2x64 import tac2x64

import subprocess
import getopt
import sys

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    file = args[0]

    if file.endswith('.bx'):
        filename = file[:-3]
    else:
        print(f'{file} does not end in .bx')
        sys.exit(1)

    with open(file, 'r') as f:
        code = f.read()

    tac_fn = filename + '.json'
    tac_file = bx2tac(code, tac_fn)

    with open(tac_fn, 'w') as file:
        file.write(tac_file)

    x64_file = tac2x64(tac_fn)
    x64_name = filename + '.s'
    f_out = open(x64_name, 'w')

    for i in x64_file:
        f_out.write(i + '\n')
    f_out.close()
    print("Success!")