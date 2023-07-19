from collections import deque

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if bugs[ny][nx] == 0:
                continue
            if bugs[ny][nx] == '1':
                bugs[ny][nx] = count
                queue.append((ny, nx))

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):

    m, n, k = map(int, input().split())
    bugs = [['0' for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        bugs[x][y] = '1'
        
    count = 0
    for h in range(n):
        for w in range(m):
            if bugs[h][w] == '1':
                bfs(h, w)
                count += 1
    
    print(count)
