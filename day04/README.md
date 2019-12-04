## Day 4

I think, this day's puzzle is easier and less interesting than previous one. We just need to check every possible password.

### Part 1

```
start = 147981
end = 691423

total = 0
for password in range(start, end):

    password_str = str(password)

    for i in range(5):
        if password_str[i] == password_str[i + 1]:
            break
    else:
        continue

    for i in range(5):
        if int(password_str[i]) > int(password_str[i + 1]):
            break
    else:
        total += 1


print(total)

```

### Part 2

```
from collections import Counter

start = 147981
end = 691423

total = 0
for password in range(start, end):

    password_str = str(password)

    for i in range(5):
        if password_str[i] == password_str[i + 1]:
            break
    else:
        continue

    for i in range(5):
        if int(password_str[i]) > int(password_str[i + 1]):
            break
    else:
        c = Counter(password_str)
        for j in c.values():
            if j == 2:
                total += 1
                break


print(total)
```