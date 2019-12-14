## Day 14

### Part 1

\Created 2 bucket one for needed ingredients, other is for ingredients we already have. Until first bucket becomes empty, we remove one item and decompile into smaller parts then put any excess material to second ingredient. If equations were very long and complicated, the order of these picking would be important. But, it doesn't matter with the given inputs. [part1.py](part1.py)

### Part 2

The same stuff combined with a binary search. [part2.py](part2.py)

```python
start = 0
end = 100_000_000_000
middle = -1

while True:
    temp = (start + end) // 2
    if temp == middle:
        break
    middle = temp

    result = calc_ore(fuel=middle)

    if result > 1e12:
        end = middle
    else:
        start = middle

if result > 1e12:
    print(middle - 1)
else:
    print(middle)
```