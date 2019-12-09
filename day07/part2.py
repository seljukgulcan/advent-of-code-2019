import sys
from itertools import permutations


def parse_instruction(instruction):
    op_code = instruction % 100

    mode = instruction // 100
    mode_1 = mode % 10
    mode //= 10
    mode_2 = mode % 10
    mode //= 10
    mode_3 = mode % 10

    return op_code, mode_1, mode_2, mode_3


def amplifier(insr_lst, phase):

    input_counter = 0

    ic = 0
    while True:
        op_code, mode_1, mode_2, mode_3 = parse_instruction(insr_lst[ic])

        if op_code == 1:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]
            addr = insr_lst[ic + 3]

            insr_lst[addr] = p_1 + p_2
            ic += 4

        elif op_code == 2:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]
            addr = insr_lst[ic + 3]

            insr_lst[addr] = p_1 * p_2
            ic += 4

        elif op_code == 3:
            addr = insr_lst[ic + 1]

            if input_counter == 0:
                result = phase
            else:
                result = input_signal

            insr_lst[addr] = result
            input_counter += 1
            ic += 2

        elif op_code == 4:
            output = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            yield output
            ic += 2

        elif op_code == 5:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]

            if p_1 != 0:
                ic = p_2
            else:
                ic += 3

        elif op_code == 6:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]

            if p_1 == 0:
                ic = p_2
            else:
                ic += 3

        elif op_code == 7:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]
            addr = insr_lst[ic + 3]

            insr_lst[addr] = 1 if p_1 < p_2 else 0
            ic += 4

        elif op_code == 8:
            p_1 = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]
            p_2 = insr_lst[ic + 2] if mode_2 else insr_lst[insr_lst[ic + 2]]
            addr = insr_lst[ic + 3]

            insr_lst[addr] = 1 if p_1 == p_2 else 0
            ic += 4

        elif op_code == 99:
            return
        else:
            # Something is wrong
            print('op_code error: {}'.format(op_code))
            sys.exit(1)


mem = list(map(int, input().split(',')))
max_output = 0


for phase_lst in permutations(range(5, 10), 5):
    amp_lst = [amplifier(mem[:], phase) for phase in phase_lst]
    input_signal = 0

    stop = False
    while not stop:
        for i in range(5):
            try:
                input_signal = next(amp_lst[i])
                if i == 4:
                    output = input_signal
            except StopIteration:
                stop = True
                break

    if output > max_output:
        max_output = output

print(max_output)
