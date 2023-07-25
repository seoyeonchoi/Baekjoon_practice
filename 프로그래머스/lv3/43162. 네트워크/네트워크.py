from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    queue = deque([])
    
    def bfs():        
        
        while queue:
            temp = queue.popleft()
            visited[temp] = 1
            
            for i in range(n):
                if visited[i] == 1:
                    continue
                elif computers[temp][i] == 1:
                    queue.append(i)
                    bfs()
        
    for k in range(n):
        if visited[k] == 0:
            queue.append(k)
            bfs()
            answer += 1
        
    return answer