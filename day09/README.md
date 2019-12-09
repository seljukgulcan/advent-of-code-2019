## Day 9

Another IntCode problem. This time, the problem ask us to implement new parameter mode called relative mode and a new operation related to this mode. The problem is not very complicated however a bug from an earlier day made me spend a lot of time on debugging. It is working good eventually. I also wrapped interpreter codes around a class, it should be much more easier to use in the following puzzles. 

Here is full specification for IntCode Interpreter (thanks [boredcircuits](https://www.reddit.com/r/adventofcode/comments/e86a28/complete_intcode_computer_spec/) from Reddit)

```
Machine State

The machine's state consists of three things:

Memory. The word size needs to be large enough to handle large numbers (though this is rather poorly defined right now).

The next instruction to execute, starting at the beginning of memory.

The "relative base" (used in parameter modes), initialized to 0.

Instruction Decoding

Instructions are encoded in base 10. Starting from the least significant digits, the first two specify the opcode. The next is the parameter mode for the first parameter, followed by the same for the second and then third parameters.

The opcodes are as follows:

1: Add the first and second parameters and store in the third.

2: Multiply the first and second parameters and store in the third.

3: Input a value and store in the first parameter.

4: Output the value in the first parameter.

5: Jump to the address in the second parameter if the first is nonzero.

6: Jump to the address in the third parameter if the first is zero.

7: If the first parameter is less than the second, store a 1 in the third parameter or 0 otherwise.

8: If the first parameter is equal to the second, store a 1 in the third parameter or 0 otherwise.

9: Add the value in the first parameter to the relative base, which becomes the new relative base.

99: Halt the program.

Instructions have variable-length encoding, based on the number of parameters of the opcode. The next instruction to execute follows the last parameter used by that instruction (except for opcodes 5 and 6, which could advance somewhere else entirely if the condition holds).

Parameter Modes

Each parameter of an instruction can have one of three modes:

0: Position Mode. The parameter encodes an address in memory where the value should be read from or written to.

1: Immediate Mode. The parameter encodes the actual value to read. Note: writing has no meaning in this mode.

2: Relative Mode. Using the relative base as an initial address in memory, the parameter encodes an offset from this address to the value to read from or write to.

Executable Format

Binaries are stored in text files where memory values are separated by commas.
```

Interpreter implementation can be found in [intcode.py](intcode.py) file. I'm planning to add a debug helper which convert intcode's into some high level instructions. Something like this:

```
 1002, 41, 29, 80      $80 <- $41 + 29
 99                    HALT
```