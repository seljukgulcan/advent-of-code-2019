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
