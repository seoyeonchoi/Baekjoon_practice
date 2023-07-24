from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(n+1)]
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

queue = deque([])

def bfs():
    while queue:
        check = queue.popleft()
        visited[check] = 1

        for c in node[check]:
            if visited[c] == 1:
                continue
            else:
                queue.append(c)
                bfs()

count = 0

for i in range(1, n+1):
    if visited[i] == 0:
        queue.append(i)
        bfs()
        count += 1
    else:
        continue

print(count)