import sys

moon_lst = []

for line in sys.stdin:
    line = line[1:-1]
    moon_lst.append(list(map(lambda x: int(x[2:-1]), line.split())))

N = len(moon_lst)

v_lst = [[0 for j in range(3)] for i in range(N)]

for t in range(1000):

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

total = 0
for i in range(N):

    potential = sum(map(abs, moon_lst[i]))
    kinetic = sum(map(abs, v_lst[i]))

    total += potential * kinetic

print(total)
