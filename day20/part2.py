from collections import defaultdict
import sys


def is_outside(row, col):
    if row == 0 or row == R - 1:
        return True
    if col == 0 or col == C - 1:
        return True
    return False


with open('input.txt') as file:
    G = [list(line)[:-1] for line in file]

R = len(G)
C = len(G[0])

letter2door_lst = defaultdict(list)

for row in range(R):
    for col in range(C):
        c = G[row][col]
        if c == '@':
            start = (row, col)
        elif c == '>':
            end = (row, col)
        elif c.isalpha():
            letter2door_lst[c].append((row, col))

way2way = dict()
for key, value in letter2door_lst.items():
    a = value[0]
    b = value[1]
    way2way[a] = b
    way2way[b] = a


D = [(-1, 0),
     (1, 0),
     (0, -1),
     (0, 1)
     ]


start = (*start, 0)
distance = 1
visited_set = set()
current_set = {start}
next_set = set()

while current_set:

    for point in current_set:

        if G[point[0]][point[1]].isalpha():

            level = point[2]
            if is_outside(point[0], point[1]):
                level -= 1
            else:
                level += 1

            warp = way2way[(point[0], point[1])]

            if level >= 0:
                next_tile = (*warp, level)

                if next_tile not in visited_set and next_tile not in current_set:
                    next_set.add(next_tile)

        visited_set.add(point)
        for drow, dcol in D:
            row = point[0] + drow
            col = point[1] + dcol
            level = point[2]

            if row < 0 or col < 0:
                continue
            if row >= R or col >= C:
                continue

            neighbor = (row, col, level)

            if neighbor in visited_set or neighbor in current_set:
                continue

            c = G[row][col]

            if c == '#' or c == ' ':
                continue
            elif c == '>' and level == 0:
                print(distance)
                sys.exit(0)

            next_set.add(neighbor)

    current_set = next_set
    next_set = set()
    distance += 1
