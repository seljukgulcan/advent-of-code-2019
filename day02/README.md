## Day 2

### Part 1

Part 1 ask us to implement a basic CPU simulation. instructions are given in a list (let's call it `mem`). Each group of 4 integer represents an instruction in the following form.

 `OP_CODE - OPERAND_1_ADDR - OPERAND_2_ADDR - STORE_ADDR`

  - if op_code is 1 then the operation is summation. `MEM[STORE_ADDR] = MEM[ADDR_1] + MEM[ADDR_2]`
  - if it is 2, the operation is multiplication `MEM[STORE_ADDR] = MEM[ADDR_1] * MEM[ADDR_2]`
  - if it is 99, we stop the program.

The puzzle asks the value of `MEM[0]`.

It is straightforward to implement.

```python
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

```

### Part 2

In part 2, puzzle asks 'which interger values of x, y where `mem[1] = x` and `mem[2] = y`, make `mem[0]` equal to given target value after running the instructions. The target value was `19690720` in my case. Intervals for `x` and `y` are also given, they are both in `[0, 100]`.

#### Brute force

For each possible `x, y` pair we can run the instructions. That is actually very simple and that is what the problem really wants us to do.

[part2_brute.py](part2_brute.py)

```python
original_lst = mem[:]
for x in range(100):
    for y in range(100):
        mem = original_lst[:]

        if run(x, y) == target:
            print('Found {}, {}'.format(x, y))
            print(100 * x + y)
            sys.exit(0)
```

#### Calculating the Closed Form

Brute force method is fine but we run the instruction set 100 * 100 times to get the answer. We can do better than that. Instead of trying every possibilities on instruction set, we can reduce these instructions into a single expression. To be able to do that, we need the following assumptions:

 1. `OP_CODE` of an instructions is never changed by an earlier instruction. (If this does not hold then final expression depends on the value of `x` and `y`)

 2. `x` and `y` do not appear as `OPERAND_ADDR`.

Although the problem description doesn't say so, input data seems to be consistent with our assumptions.

```
OP_CODE ADDR ADDR STORE_ADDR
1       x    y    3
1       1    2    3
1       3    4    3
1       5    0    3
2       10   1    19
1       6    19   23
2       23   6    27
1       5    27   31
1       31   9    35
2       10   35   39
1       5    39   43
2       43   10   47
1       47   6    51
2       51   6    55
.
.
.
99
```

Store addresses are always in `4k - 1` form and operation codes are in `4k`th indices so assumption 1 is ok.

Assumption 2 is problematic because first instruction uses them. However, if we look at second instruction, we can see that the result of first instruction is overwritten by second instruction. So, we can skip first instruction to hold assumption 2 true.

After running instruction with `x` and `y` terms, the final expression becomes `614400*x + y + 644274`. Now we can loop over interval to find x and y.

I code these symbol operations from scratch in [part2_expr.py](part2_expr.py). It was not the greatest idea, code looks horrible but it works!. Probably, I need to refactor it later (I will not). [part2_sympy.py](part2_sympy.py) contains the same procedure with sympy's symbolic operations.