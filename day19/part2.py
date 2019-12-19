from intcode import Interpreter
from collections import defaultdict
import copy


def is_illuminated(x, y):
    intcode_output = -1

    def process_output(output):
        nonlocal intcode_output
        intcode_output = output

    mem_copy = copy.copy(mem)
    program = Interpreter(mem_copy)
    program.run(input_signal=iter([x, y]), process_output=process_output)

    if intcode_output == 1:
        return True
    elif intcode_output == 0:
        return False
    else:
        raise ValueError('Unexpected intcode output')


def check(x):
    y = 0
    while True:
        if(is_illuminated(x, y)):
            break
        y += 1
    while True:
        if not is_illuminated(x, y):
            break
        y += 1

    y -= 1

    for i in range(100):
        if not is_illuminated(x + i, y - i):
            return False
    if is_illuminated(x + 100, y - 100):
        return False

    print(x * 10000 + y - 99)

    return True


mem = defaultdict(int)
with open('input.txt') as file:
    for key, value in enumerate(map(int, file.readline().split(','))):
        mem[key] = value


print(check(1328))
print(check(1329))
print(check(1330))
print(check(1331))
