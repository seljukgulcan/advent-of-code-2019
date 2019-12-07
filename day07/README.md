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

#### Multiprocessing

Just implemeted it with multiprocessing. It creates 5 processes for each permutation. It is terrible in terms of elapsed time but it simulates interpreters as it is told in the problem description and I found a change to learn a few things along the way. The main function looks like this:

```python
    result = multiprocessing.Value('i')
    mem = list(map(int, input().split(',')))

    max_value = 0

    for phase_lst in permutations(range(5, 10), 5):

        result.value = 0
        recv_pipe_lst = []
        send_pipe_lst = []

        for i in range(5):
            recv, send = multiprocessing.Pipe()
            recv_pipe_lst.append(recv)
            send_pipe_lst.append(send)

        p_lst = []
        phase = 1
        for i, phase in enumerate(phase_lst):
            recv = recv_pipe_lst[i]
            send = send_pipe_lst[(i + 1) % 5]
            initial_input = 0 if i == 0 else None
            send_result = True if i == 4 else False
            p = multiprocessing.Process(
                target=amplifier, args=(mem[:], phase, initial_input, recv, send, send_result, result))
            p.start()
            p_lst.append(p)

        p_lst[0].join()
        for i in range(1, 5):
            p_lst[i].terminate()

        if result.value > max_value:
            max_value = result.value

    print(max_value)
```