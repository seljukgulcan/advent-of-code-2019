import sys

target = 19690720
mem = list(map(int, input().split(',')))


def run(noun, verb):

    mem[1] = noun
    mem[2] = verb

    for i in range(0, len(mem), 4):
        op_code = mem[i]

        if op_code == 99:
            break

        left_val = mem[mem[i + 1]]
        right_val = mem[mem[i + 2]]

        if op_code == 1:
            result = left_val + right_val
        elif op_code == 2:
            result = left_val * right_val
        else:
            # Something is wrong
            print('op_code error')
            sys.exit(1)

        mem[mem[i + 3]] = result

    return mem[0]


original_lst = mem[:]
for x in range(100):
    for y in range(100):
        mem = original_lst[:]

        if run(x, y) == target:
            print('Found {}, {}'.format(x, y))
            print(100 * x + y)
            sys.exit(0)
