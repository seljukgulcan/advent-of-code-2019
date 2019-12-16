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
