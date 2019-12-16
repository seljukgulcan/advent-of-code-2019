## Day 16

### Part 1

Part 1 is easy, I created a tranformation matrix from described pattern. Then, everything else is simple matrix operations. [part1.py](part1.py) takes around 300 msecs.

```python
import numpy as np

digit_str = input().strip()
digit_lst = list(map(int, digit_str))

N = len(digit_lst)

M = np.empty((N, N), dtype=int)

pattern = [0, 1, 0, -1]

for i in range(N):

    for j in range(N):

        index = (j + 1) // (i + 1)
        index %= len(pattern)

        M[i, j] = pattern[index]

digit_vec = np.array(digit_lst)

for i in range(100):
    digit_vec = np.abs(M @ digit_vec) % 10

result = digit_vec[:8]
print(*result, sep='')
```

### Part 2

This is too big to calculate using previous method. Actually, I couldn't figure it out this part by myself, I checked it on Reddit. 

**Observation 1**

for digits i > N / 2, their multiplier pattern is as follows :

`0 0 0 0 0 0 ... 0 1 1 1 1 . . . 1`

The index of first 1 is i, so we just need to calculate `sum(vector[i:])` for i > N / 2

**Observation 2**

The indices of the requested digits are greater than N / 2. For my case this offset is `5976963` and N is `6500000` but I guess, this is true for all inputs.

Combining these observations, algorithm becomes as follows :

 - repeat 100 times :
   - for i from last index to offset :
     - Calculate cumulative sum
     - Set next digit = cumulative sum

```python
digit_str = input().strip()
digit_lst = list(map(int, digit_str)) * 10000

offset = int(digit_str[:7])

digit_vec = digit_lst[offset:]

for i in range(100):
    csum = 0
    for j in reversed(range(len(digit_vec))):
        csum += digit_vec[j]
        digit_vec[j] = abs(csum) % 10

result = digit_vec[:8]
print(*result, sep='')
```

This [part](part2.py) takes around 11 seconds to complete.
