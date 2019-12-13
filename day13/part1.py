from intcode import Interpreter
from collections import defaultdict


def store(output):
    output_lst.append(output)


mem = defaultdict(int)
for key, value in enumerate(map(int, input().split(','))):
    mem[key] = value

output_lst = []
p = Interpreter(mem)
p.run(process_output=store)

count = 0
for i in range(0, len(output_lst), 3):
    if output_lst[i + 2] == 2:
        count += 1

print(count)
