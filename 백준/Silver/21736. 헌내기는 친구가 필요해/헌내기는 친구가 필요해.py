from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = []

for _ in range(n):
    map.append(list(input()))


for i in range(n):
    for k in range(m):
        if map[i][k] == 'I':
            start = (i, k)

visited = [[0 for _ in range(m)] for _ in range(n)]

count = 0

def bfs():
    global count
    queue = deque()
    queue.append(start)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map[nx][ny] == 'X':
                continue
            if map[nx][ny] == 'O' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
            if map[nx][ny] == 'P' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                queue.append((nx, ny))


bfs()
if count > 0:
    print(count)
else:
    print('TT')