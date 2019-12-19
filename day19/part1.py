from intcode import Interpreter
from collections import defaultdict
from itertools import product
import copy

total = 0


def process_output(output):
    global total
    total += output


mem = defaultdict(int)
with open('input.txt') as file:
    for key, value in enumerate(map(int, file.readline().split(','))):
        mem[key] = value


for x, y in product(range(50), repeat=2):
    mem_copy = copy.copy(mem)
    program = Interpreter(mem_copy)
    program.run(input_signal=[x, y], process_output=process_output)

print(total)
