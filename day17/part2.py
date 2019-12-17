from collections import defaultdict
from intcode import Interpreter


def input_signal():

    signal = 'A,C,A,B,A,C,B,C,B,C\n'
    signal += 'R,8,L,10,L,12,R,4\n'
    signal += 'R,8,L,10,R,8\n'
    signal += 'R,8,L,12,R,4,R,4\n'
    signal += 'n\n'
    for c in signal:
        yield ord(c)


mem = defaultdict(int)
with open('input.txt') as file:
    for key, value in enumerate(map(int, file.readline().split(','))):
        mem[key] = value

mem[0] = 2

program = Interpreter(mem)

program.run(input_signal=input_signal())
