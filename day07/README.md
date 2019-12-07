## Day 7

### Part 1

Another IntCode Interpreter problem. First part asks to connect 5 interpreter back to back. The output of one becomes the input of another. Small adjustment to part 5's interpreter gave the result.

### Part 2

This is an interesting one. Now, we connect interpreter 5 to interpreter 1 to form a feedback loop. So, after sending its output to interpreter 2, interpreter 1 needs to wait until the input from interpreter 5 is arrived. At first, it seems difficult to do without any concurrency but then I find out that is exactly what generators are for. What I did is simply as follows: Changed `return` to `yield` in output opcode and `exit` to `return` in halting opcode. After that main loop becomes as trivial as:

```python
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
```

I'm planning to reimplement part 2 with some concurrency (`asyncio` or multithreading). I'll update if I complete that.