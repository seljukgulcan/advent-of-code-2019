import sys

mem = list(map(int, input().split(',')))

input_val = 1

i = 0
while True:
    op_code = mem[i] % 100

    if op_code == 99:
        break

    if op_code == 1 or op_code == 2:

        mode = mem[i] // 100
        mode_1 = mode % 10
        mode //= 10
        mode_2 = mode % 10
        mode //= 10
        mode_3 = mode // 10

        p_1 = mem[i + 1] if mode_1 else mem[mem[i + 1]]
        p_2 = mem[i + 2] if mode_2 else mem[mem[i + 2]]
        addr = mem[i + 3]

        if op_code == 1:
            result = p_1 + p_2
        else:
            result = p_1 * p_2

        mem[addr] = result

        i += 4
    elif op_code == 3:
        addr = mem[i + 1]
        mem[addr] = input_val
        i += 2
    elif op_code == 4:
        addr = mem[i + 1]

        mode = (mem[i] // 100) % 10
        output = mem[i + 1] if mode else mem[mem[i + 1]]

        print(output)
        i += 2
    else:
        # Something is wrong
        print('op_code error: {}'.format(op_code))
        sys.exit(1)
