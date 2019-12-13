from typing import DefaultDict, Tuple, Union, Generator, Callable


class Interpreter:
    '''
    IntCode Intpreter for AoC2019
    '''

    def __init__(self, mem: DefaultDict[int, int]):
        self.mem = mem
        self.rc = 0  # Relative Counter

    @staticmethod
    def _parse(instruction: int) -> Tuple[int, int, int, int]:
        '''
        Parses given instruction, ABCDE as follows
        DE -> op_code
        C  -> mode for first parameter
        B  -> mode for second parameter
        A  -> mode for third parameter
        '''
        op_code = instruction % 100

        mode = instruction // 100
        mode_1 = mode % 10
        mode //= 10
        mode_2 = mode % 10
        mode //= 10
        mode_3 = mode % 10

        return op_code, mode_1, mode_2, mode_3

    def _ind(self, index: int, mode: int) -> int:
        '''
        Returns parameter for given index and mode
        mode 0: Default mode
        mode 1: Immediate mode
        mode 2: Relative mode
        '''
        if mode == 0:
            return self.mem[index]
        if mode == 1:
            return index
        if mode == 2:
            return self.mem[index] + self.rc

        raise ValueError('Invalid mode: {}'.format(mode))

    def run(self, input_signal: Union[int, Generator[int, None, None]] = 0,
            process_output: Callable[[int], None] = print):
        '''
        If input_signal is integer, all input operations will use this signal.
        If it is a generator, next value of it will be used each time
        '''
        mem = self.mem
        ind = self._ind

        ic = 0
        while True:
            op_code, mode_1, mode_2, mode_3 = self._parse(mem[ic])

            if op_code == 1:
                # Addition Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]
                addr = ind(ic + 3, mode_3)

                mem[addr] = p_1 + p_2
                ic += 4

            elif op_code == 2:
                # Multiplication Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]
                addr = ind(ic + 3, mode_3)

                mem[addr] = p_1 * p_2
                ic += 4

            elif op_code == 3:
                # Input Operation
                addr = ind(ic + 1, mode_1)

                if isinstance(input_signal, int):
                    value = input_signal
                else:
                    value = next(input_signal)

                mem[addr] = value
                ic += 2

            elif op_code == 4:
                # Output Operation
                output = mem[ind(ic + 1, mode_1)]

                process_output(output)
                ic += 2

            elif op_code == 5:
                # JumpIfNotZero Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]

                if p_1 != 0:
                    ic = p_2
                else:
                    ic += 3

            elif op_code == 6:
                # JumpIfZero Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]

                if p_1 == 0:
                    ic = p_2
                else:
                    ic += 3

            elif op_code == 7:
                # SetLessThan Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]
                addr = ind(ic + 3, mode_3)

                mem[addr] = 1 if p_1 < p_2 else 0
                ic += 4

            elif op_code == 8:
                # SetEquals Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                p_2 = mem[ind(ic + 2, mode_2)]
                addr = ind(ic + 3, mode_3)

                mem[addr] = 1 if p_1 == p_2 else 0
                ic += 4

            elif op_code == 9:
                # IncrementRelativeCounter Operation
                p_1 = mem[ind(ic + 1, mode_1)]
                self.rc += p_1

                ic += 2

            elif op_code == 99:
                # Halting Operation
                break
            else:
                # Unknown Opcode
                raise ValueError('op_code error: {}'.format(op_code))
