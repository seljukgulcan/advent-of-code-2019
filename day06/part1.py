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
