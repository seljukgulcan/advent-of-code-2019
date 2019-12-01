import sys

total = 0
for line in sys.stdin:
	total += int(line) // 3 - 2
print(total)
