from intcode import Interpreter
from collections import defaultdict

screen = None

paddle_x = None
ball_x = None
screen = [[-1 for j in range(38)] for i in range(22)]
score = -1


def store(output):
    output_lst.append(int(output))


def process_output(draw=False):
    global ball_x
    global paddle_x
    global score

    for i in range(0, len(output_lst), 3):
        x = output_lst[i]
        y = output_lst[i + 1]
        idx = output_lst[i + 2]

        if x == -1 and y == 0:
            score = idx

        else:
            pivot = ' '

            if idx == 1:
                pivot = '+'
            elif idx == 2:
                pivot = 'X'
            elif idx == 3:
                pivot = '='
                paddle_x = x
            elif idx == 4:
                pivot = 'O'
                ball_x = x

            screen[y][x] = pivot

    # Show
    if draw:
        for row in screen:
            print(*row, sep='')
        print('---')
        print(score)


def input_signal():

    while True:
        process_output(draw=False)
        if paddle_x > ball_x:
            signal = -1
        elif paddle_x == ball_x:
            signal = 0
        else:
            signal = 1

        output_lst.clear()
        yield signal


mem = defaultdict(int)
for key, value in enumerate(map(int, input().split(','))):
    mem[key] = value

output_lst = []

mem[0] = 2
p = Interpreter(mem)
p.run(input_signal=input_signal(), process_output=store)
process_output(draw=False)

print(score)
