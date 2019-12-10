import sys
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

R = 29
C = 26
G[R][C] = 'O'

for i, j in ast_lst:
    if R == i and C == j:
        continue

    drow = i - R
    dcol = j - C

    gcd = math.gcd(drow, dcol)
    drow = drow // gcd
    dcol = dcol // gcd

    ii = i + drow
    jj = j + dcol

    while inside(ii, jj):
        G[ii][jj] = 'X'
        ii = ii + drow
        jj = jj + dcol


lst = []
for i in range(N):
    for j in range(M):
        if G[i][j] == '#':
            ii = i - R
            jj = j - C

            # Convert to x, y coordinates
            x = jj
            y = -1 * ii

            if y == 0:
                angle = math.pi / 2 if x > 0 else 3 * math.pi / 2
            else:
                angle = (math.atan(x / y) + math.pi) % math.pi
                if x < 0:
                    angle += math.pi

            lst.append((angle, i, j))

lst.sort()

angle, y, x = lst[199]
result = x * 100 + y
print(result)
