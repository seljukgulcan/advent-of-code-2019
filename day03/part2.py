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
    count = 0
    for move in move_lst:
        d = move[0]
        step_count = int(move[1:])

        dx, dy, is_horizontal = d_lst[d]
        start = (x + dx, y + dy)
        end = (x + step_count * dx, y + step_count * dy)

        line_lst.append(Line(start, end, is_horizontal, count))
        x, y = end
        count += step_count

    # Second Line
    move_lst = input().split(',')

    x = 0
    y = 0
    count = 0
    for move in move_lst:
        d = move[0]
        step_count = int(move[1:])

        dx, dy, is_horizontal = d_lst[d]
        start = (x + dx, y + dy)
        end = (x + step_count * dx, y + step_count * dy)

        line2 = Line(start, end, is_horizontal, count)

        for line in line_lst:

            point_lst = line.intersect(line2)

            for point in point_lst:
                distance = line.count + find_distance(line.start, point) + 1
                distance += line2.count + find_distance(line2.start, point) + 1

                min_distance = min(min_distance, distance)

        x, y = end
        count += step_count

    print(min_distance)
