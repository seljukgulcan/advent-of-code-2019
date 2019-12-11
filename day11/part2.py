from collections import defaultdict
from intcode import Interpreter

# Global State
row = 150
col = 150
output_counter = 0
current = 0


def paint():
    while True:
        yield G[row][col]


def process_output(output):

    global row, col, output_counter, current

    if output_counter == 0:
        G[row][col] = output
    else:
        if current == 0:
            if output == 0:
                current = 1
                col -= 1
            else:
                current = 3
                col += 1
        elif current == 1:
            if output == 0:
                current = 2
                row += 1
            else:
                current = 0
                row -= 1
        elif current == 2:
            if output == 0:
                current = 3
                col += 1
            else:
                current = 1
                col -= 1
        elif current == 3:
            if output == 0:
                current = 0
                row -= 1
            else:
                current = 2
                row += 1

    output_counter += 1
    output_counter %= 2


if __name__ == '__main__':

    mem = defaultdict(int)
    for key, value in enumerate(map(int, input().split(','))):
        mem[key] = value

    G = [[0 for j in range(300)] for i in range(300)]
    G[row][col] = 1

    program = Interpreter(mem)
    program.run(input_signal=paint(), process_output=process_output)

    import numpy as np
    import matplotlib.pyplot as plt

    im = np.array(G)

    plt.imshow(im, cmap='gray')
    plt.tight_layout()
    plt.axis('off')
    plt.show()
