from collections import Counter

s = input()

size = 25 * 6
layer_count = len(s) // size

layer_lst = [list(map(int, (s[size * i:size * (i + 1)])))
             for i in range(layer_count)]

counter_lst = [Counter(layer) for layer in layer_lst]

min_counter = None
min_count = float('inf')

for counter in counter_lst:
    if counter[0] < min_count:
        min_count = counter[0]
        min_counter = counter

result = min_counter[1] * min_counter[2]
print(result)
