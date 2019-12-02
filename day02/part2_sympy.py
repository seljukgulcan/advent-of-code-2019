import sys
import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')

mem = list(map(int, input().split(',')))

mem[1] = x
mem[2] = y

for i in range(4, len(mem), 4):
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

final_expression = mem[0]
print(final_expression)

for x_val in range(100):
    for y_val in range(100):
        if final_expression.subs([(x, x_val), (y, y_val)]) == 19690720:

            print('Found {}, {}'.format(x_val, y_val))
            print(100 * x_val + y_val)
            sys.exit(0)
