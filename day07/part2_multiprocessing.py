import multiprocessing
import sys
from itertools import permutations


def parse_instruction(instruction):
    op_code = instruction % 100

    mode = instruction // 100
    mode_1 = mode % 10
    mode //= 10
    mode_2 = mode % 10
    mode //= 10
    mode_3 = mode // 10

    return op_code, mode_1, mode_2, mode_3


def amplifier(insr_lst, phase, initial_input, recv, send, send_result=False, result=None):
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
                value = phase
            elif input_counter == 1 and initial_input is not None:
                value = initial_input
            else:
                value = recv.recv()

            insr_lst[addr] = value
            input_counter += 1
            ic += 2

        elif op_code == 4:
            output = insr_lst[ic + 1] if mode_1 else insr_lst[insr_lst[ic + 1]]

            if send_result:
                result.value = output

            send.send(output)
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


if __name__ == '__main__':

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
                target=amplifier, args=(mem, phase, initial_input, recv, send, send_result, result))
            p.start()
            p_lst.append(p)

        p_lst[0].join()
        for i in range(1, 5):
            p_lst[i].terminate()

        if result.value > max_value:
            max_value = result.value

    print(max_value)
