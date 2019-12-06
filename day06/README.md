## Day 5

### Part 1

Given a DAG, the question is what is the total distance to root for each node. I solved it with DFS:

```python
import sys
from collections import defaultdict


def DFS(u, count=0):

    retval = count
    for v in G[u]:
        retval += DFS(v, count + 1)

    return retval


G = defaultdict(list)

for line in sys.stdin:
    u, v = line.strip().split(')')
    G[u].append(v)

result = DFS('COM')
print(result)
```

### Part 2

In part 2, the distance between two specific node is asked. Again, the same DFS approach with small adjustment gave the solution.

```python
import sys
from collections import defaultdict


def DFS(u, count=0):

    if u == 'SAN':
        return count

    for v in G[u]:

        if v in visited_set:
            continue

        visited_set.add(v)

        found = DFS(v, count + 1)
        if found:
            return found

    return False


G = defaultdict(list)
visited_set = {'YOU'}

for line in sys.stdin:
    u, v = line.strip().split(')')
    G[u].append(v)
    G[v].append(u)


result = DFS('YOU')
print(result - 2)
```