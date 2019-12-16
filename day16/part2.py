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
