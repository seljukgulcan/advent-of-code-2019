import sys
from fractions import Fraction

G = []

for line in sys.stdin:
    G.append(list(line.strip()))

ast_lst = []

N = len(G)
M = len(G[0])

for i in range(N):
    for j in range(M):
        if G[i][j] == '#':
            ast_lst.append((i, j))

max_val = 0
max_point = None

for row, col in ast_lst:

    left_set = set()
    right_set = set()

    for i, j in ast_lst:
        if row == i and col == j:
            continue

        # Convert (i, j) to x and y centered around chosen asteroid
        x = j - col
        y = -1 * (i - row)

        if x < 0:
            if y == 0:
                left_set.add(float('inf'))
            else:
                angle = Fraction(x, y)
                left_set.add(angle)
        elif x > 0:
            if y == 0:
                right_set.add(float('inf'))
            else:
                angle = Fraction(x, y)
                right_set.add(angle)
        else:
            # x == 0
            if y < 0:
                left_set.add(Fraction(x, y))
            else:
                right_set.add(Fraction(x, y))

        count = len(left_set) + len(right_set)
        if count > max_val:
            max_val = count
            max_point = (row, col)

print(max_val)
print(max_point)
