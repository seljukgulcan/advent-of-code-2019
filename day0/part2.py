import sys

total = 0

frequency_set = set()
frequency_set.add(0)

change_lst = list(int(line) for line in sys.stdin)

found = False
while not found:
	for change in change_lst:

		total += change

		if total in frequency_set:
			print(total)
			found = True
			break

		frequency_set.add(total)
