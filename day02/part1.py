import sys

mem = list(map(int, input().split(',')))

mem[1] = 12
mem[2] = 2

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

print(mem[0])
