from collections import defaultdict
from intcode import Interpreter

G = []
row = []


def process_output(output):

    c = chr(output)

    if c == '\n':
        if row:
            G.append(row[:])
        row.clear()
    else:
        row.append(c)


mem = defaultdict(int)
with open('input.txt') as file:
    for key, value in enumerate(map(int, file.readline().split(','))):
        mem[key] = value

program = Interpreter(mem)

program.run(process_output=process_output)

for row in G:
    print(*row, sep='')

R = len(G)
C = len(G[0])

total = 0

D = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

for r in range(R):
    for c in range(C):
        if G[r][c] == '.':
            continue

        neighbor_count = 0
        for drow, dcol in D:

            n_r = r + drow
            n_c = c + dcol

            if n_r >= R or n_c >= C:
                continue
            if n_r < 0 or n_c < 0:
                continue

            if G[n_r][n_c] != '.':
                neighbor_count += 1

        if neighbor_count >= 3:

            total += r * c

print(total)
