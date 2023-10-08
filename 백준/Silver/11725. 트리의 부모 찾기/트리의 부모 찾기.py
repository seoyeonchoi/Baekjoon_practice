import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
node = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

parents = [0 for _ in range(n+1)]


def bfs(x):
    queue = deque([])
    queue.append(x)
    parents[x] = 1

    while queue:
        nx = queue.popleft()
        for each in node[nx]:
            if parents[each] == 0:
                parents[each] = nx
                queue.append(each)

bfs(1)
for i in range(2, n + 1):
    print(parents[i])
