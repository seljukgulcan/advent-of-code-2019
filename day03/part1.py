from common import *

d_lst = {
    'U': (0, 1, False),
    'R': (1, 0, True),
    'D': (0, -1, False),
    'L': (-1, 0, True)
}


if __name__ == '__main__':

    move_lst = input().split(',')

    line_lst = []

    min_distance = float('inf')

    x = 0
    y = 0
    for move in move_lst:
        d = move[0]
        step_count = int(move[1:])

        dx, dy, is_horizontal = d_lst[d]
        start = (x + dx, y + dy)
        end = (x + step_count * dx, y + step_count * dy)

        line_lst.append(Line(start, end, is_horizontal))
        x, y = end

    # Second Line
    move_lst = input().split(',')

    x = 0
    y = 0
    for move in move_lst:
        d = move[0]
        step_count = int(move[1:])

        dx, dy, is_horizontal = d_lst[d]
        start = (x + dx, y + dy)
        end = (x + step_count * dx, y + step_count * dy)

        line2 = Line(start, end, is_horizontal)

        for line in line_lst:
            point_lst = line.intersect(line2)
            for point in point_lst:
                distance = find_distance((0, 0), point)
                min_distance = min(min_distance, distance)

        x, y = end

    print(min_distance)
