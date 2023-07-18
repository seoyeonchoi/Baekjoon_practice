from collections import deque

n = int(input())
count = 1
graph = []
result = []

def bfs(x, y):
    each_count = 0
    queue = deque()
    queue.append((x, y))
    
    
    while queue:
        x, y = queue.popleft()
        graph[x][y] = count
        each_count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == '0':
                continue
            if graph[nx][ny] == '1':
                graph[nx][ny] = count
                queue.append((nx, ny))
                
    return each_count

for _ in range(n):
    graph.append(list(input()))
    
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for w in range(n):
    for h in range(n):
        if graph[w][h] == '1':
            each = bfs(w, h)
            result.append(each)
            count += 1

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])