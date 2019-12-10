import sys
import copy
import math


def inside(row, col):
    if row < 0 or col < 0:
        return False
    if row >= N or col >= M:
        return False
    return True


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
    GG = copy.deepcopy(G)

    for i, j in ast_lst:
        if row == i and col == j:
            continue

        drow = i - row
        dcol = j - col

        if drow == 0:
            dcol = 1 if dcol > 0 else -1
        elif dcol == 0:
            drow = 1 if drow > 0 else -1
        else:
            gcd = math.gcd(drow, dcol)
            drow = drow // gcd
            dcol = dcol // gcd

        ii = i + drow
        jj = j + dcol

        while inside(ii, jj):
            GG[ii][jj] = 'X'
            ii = ii + drow
            jj = jj + dcol

    GG[row][col] = 'O'
    count = 0
    for i in range(N):
        for j in range(M):
            if GG[i][j] == '#':
                count += 1

    if count > max_val:
        max_val = count
        max_point = (row, col)

print(max_val)
print(max_point)
