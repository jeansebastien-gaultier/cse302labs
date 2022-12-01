#! /usr/bin/env python3

# --------------------------------------------------------------------
import abc
import sys

from typing import List

# --------------------------------------------------------------------
class BFError(Exception):
    pass

# --------------------------------------------------------------------
class BFExit(Exception):
    pass

# --------------------------------------------------------------------
class BFMemory:
    def __init__(self, memsize = 30000):
        self._memory = [0] * max(memsize, 1)
        self._ptr    = 0

    position = property(lambda self : self._ptr)

    def get(self):
        return self._memory[self._ptr]

    def set(self, value):
        self._memory[self._ptr] = int(value) & 0xff

    def increment(self):
        self.set(self.get() + 1)

    def decrement(self):
        self.set(self.get() - 1)

    def forward(self):
        self._ptr = (self._ptr + 1) % len(self._memory)

    def backward(self):
        self._ptr = (self._ptr - 1) % len(self._memory)

    def dump(self):
        import hexdump
        hexdump.hexdump(bytes(self._memory))

# --------------------------------------------------------------------
class BFInstruction(abc.ABC):
    @abc.abstractmethod
    def execute(self, memory : BFMemory):
        pass

    @staticmethod
    def parse(program : str, leniant : bool = True):
        stack = [[]]

        for c in program:
            if c == '+':
                stack[-1].append(BFIncrement())
            elif c == '-':
                stack[-1].append(BFDecrement())
            elif c == '>':
                stack[-1].append(BFForward())
            elif c == '<':
                stack[-1].append(BFBackward())
            elif c == '.':
                stack[-1].append(BFPrint())
            elif c == ',':
                stack[-1].append(BFInput())
            elif c == '[':
                stack.append([])
            elif c == ']':
                if len(stack) < 2:
                    raise BFError
                stack[-2].append(BFLoop(BFBlock(stack.pop())))
            elif not (c.isspace() or leniant):
                    raise BFError

        if len(stack) != 1:
            raise BFError

        return BFBlock(stack.pop())

# --------------------------------------------------------------------
class BFIncrement(BFInstruction):
    def execute(self, memory : BFMemory):
        memory.increment()

# --------------------------------------------------------------------
class BFDecrement(BFInstruction):
    def execute(self, memory : BFMemory):
        memory.decrement()

# --------------------------------------------------------------------
class BFForward(BFInstruction):
    def execute(self, memory : BFMemory):
        memory.forward()

# --------------------------------------------------------------------
class BFBackward(BFInstruction):
    def execute(self, memory : BFMemory):
        memory.backward()

# --------------------------------------------------------------------
class BFLoop(BFInstruction):
    def __init__(self, body : BFInstruction):
        self._body = body

    body = property(lambda self : self._body)

    def execute(self, memory : BFMemory):
        while memory.get():
            self.body.execute(memory)

# ---------------------------------------------------------------------
class BFPrint(BFInstruction):
    def execute(self, memory : BFMemory):
        sys.stdout.write(chr(memory.get()))
        sys.stdout.flush()

# --------------------------------------------------------------------
class BFInput(BFInstruction):
    def execute(self, memory : BFMemory):
        c = sys.stdin.buffer.read(1)

        if len(c) == 0:
            raise BFExit
        memory.set(ord(c))

# --------------------------------------------------------------------
class BFBlock(BFInstruction):
    def __init__(self, block : List[BFInstruction]):
        self._block = block

    block = property(lambda self : self._block)

    def execute(self, memory : BFMemory):
        for instruction in self.block:
            instruction.execute(memory)

# --------------------------------------------------------------------
def _main():
    if len(sys.argv)-1 != 1:
        print(f'Usage: {sys.argv[0]} [FILE.bf]', file = sys.stderr)
        exit(1)

    with open(sys.argv[1]) as stream:
        program = stream.read()
    program = BFInstruction.parse(program)

    try:
        program.execute(BFMemory())
    except BFExit:
        pass

# --------------------------------------------------------------------
if __name__ == '__main__':
    _main()
