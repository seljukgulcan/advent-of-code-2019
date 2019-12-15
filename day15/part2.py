from collections import defaultdict
from intcode import Interpreter


def BFS(start):
    distance = 0
    visited_set = set()
    current_set = {start}
    next_set = set()

    while current_set:

        for point in current_set:

            visited_set.add(point)
            for drow, dcol in D[1:]:
                row = point[0] + drow
                col = point[1] + dcol

                if G[row][col] == '#':
                    continue

                neighbor = (row, col)

                if neighbor in visited_set or neighbor in current_set:
                    continue

                next_set.add(neighbor)

        current_set = next_set
        next_set = set()
        distance += 1

    return distance - 1


N = 50
G = [[' ' for j in range(N)] for i in range(N)]
current = [N // 2, N // 2]
start_point = tuple(current[:])
end_point = None
last_signal = None
stop = False
has_moved = False

D = [None,
     (-1, 0),
     (1, 0),
     (0, -1),
     (0, 1)
     ]

input_cycle = [3, 1, 4, 2]
success = False


def print_map():
    for row in G:
        print(*row, sep='')


def input_signal():
    global last_signal

    index = 0

    while True:

        if stop:
            yield Interpreter.STOP_SIGNAL

        signal = input_cycle[index]

        last_signal = signal

        yield signal

        if success:
            if last_signal == 1:
                index = 0
            elif last_signal == 2:
                index = 2
            elif last_signal == 3:
                index = 3
            else:
                index = 1
        else:
            index = (index + 1) % 4


def process_output(output):
    global success, stop, has_moved, end_point

    drow, dcol = D[last_signal]

    to_move_row = current[0] + drow
    to_move_col = current[1] + dcol

    success = True
    if output == 0:
        G[to_move_row][to_move_col] = '#'
        success = False
    elif output == 1:
        has_moved = True
        G[to_move_row][to_move_col] = '.'
        current[0] = to_move_row
        current[1] = to_move_col
    else:
        has_moved = True
        G[to_move_row][to_move_col] = '$'
        current[0] = to_move_row
        current[1] = to_move_col
        end_point = tuple(current[:])

    if current[0] == start_point[0] and current[1] == start_point[1] and has_moved:
        stop = True


mem = defaultdict(int)
with open('input.txt') as file:
    for key, value in enumerate(map(int, file.readline().split(','))):
        mem[key] = value

program = Interpreter(mem)


program.run(input_signal(), process_output)
print_map()

result = BFS(end_point)
print(result)
