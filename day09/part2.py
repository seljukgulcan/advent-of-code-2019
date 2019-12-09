from collections import defaultdict
from intcode import Interpreter

if __name__ == '__main__':

    mem = defaultdict(int)
    for key, value in enumerate(map(int, input().split(','))):
        mem[key] = value

    program = Interpreter(mem)
    program.run(input_signal=2)
