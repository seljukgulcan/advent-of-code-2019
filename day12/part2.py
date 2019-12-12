import sys
import math

moon_lst = []

for line in sys.stdin:
    line = line[1:-1]
    moon_lst.append(list(map(lambda x: int(x[2:-1]), line.split())))

N = len(moon_lst)

initial_lst = [moon_lst[i][:] for i in range(N)]

v_lst = [[0 for j in range(3)] for i in range(N)]

k2period = dict()

for t in range(10000000):

    for i in range(N):
        for j in range(i + 1, N):

            pos_i = moon_lst[i]
            pos_j = moon_lst[j]

            for k in range(3):
                if pos_i[k] < pos_j[k]:
                    v_lst[i][k] += 1
                    v_lst[j][k] -= 1
                elif pos_i[k] > pos_j[k]:
                    v_lst[i][k] -= 1
                    v_lst[j][k] += 1

    for i in range(N):
        for k in range(3):
            moon_lst[i][k] += v_lst[i][k]

    for k in range(3):

        if k in k2period:
            continue

        equal = True
        for i in range(N):
            if moon_lst[i][k] != initial_lst[i][k]:
                equal = False
                break

        if equal:
            k2period[k] = t + 2

    if len(k2period) == 3:
        break

a, b, c = k2period.values()

d = (a * b) // math.gcd(a, b)

result = (c * d) // math.gcd(c, d)

print(result)
