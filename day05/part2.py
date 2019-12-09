import sys


def parse_instruction(instruction):
    op_code = instruction % 100

    mode = instruction // 100
    mode_1 = mode % 10
    mode //= 10
    mode_2 = mode % 10
    mode //= 10
    mode_3 = mode % 10

    return op_code, mode_1, mode_2, mode_3


mem = list(map(int, input().split(',')))

input_val = 5

ic = 0
while True:
    op_code, mode_1, mode_2, mode_3 = parse_instruction(mem[ic])

    if op_code == 1:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]
        addr = mem[ic + 3]

        mem[addr] = p_1 + p_2
        ic += 4

    elif op_code == 2:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]
        addr = mem[ic + 3]

        mem[addr] = p_1 * p_2
        ic += 4

    elif op_code == 3:
        addr = mem[ic + 1]
        mem[addr] = input_val
        ic += 2

    elif op_code == 4:
        output = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        print(output)
        ic += 2

    elif op_code == 5:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]

        if p_1 != 0:
            ic = p_2
        else:
            ic += 3

    elif op_code == 6:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]

        if p_1 == 0:
            ic = p_2
        else:
            ic += 3

    elif op_code == 7:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]
        addr = mem[ic + 3]

        mem[addr] = 1 if p_1 < p_2 else 0
        ic += 4

    elif op_code == 8:
        p_1 = mem[ic + 1] if mode_1 else mem[mem[ic + 1]]
        p_2 = mem[ic + 2] if mode_2 else mem[mem[ic + 2]]
        addr = mem[ic + 3]

        mem[addr] = 1 if p_1 == p_2 else 0
        ic += 4

    elif op_code == 99:
        break
    else:
        # Something is wrong
        print('op_code error: {}'.format(op_code))
        sys.exit(1)
