from collections import deque

def dfs(x):
    visited[x] = 1
    result_dfs.append(x)

    for n in nums[x]:
        if visited[n] == 0:
            dfs(n)
    
    return result_dfs

def bfs(start):
    queue.append(start)

    while queue:
        # print(queue)
        # print(visited)
        temp = queue.popleft()
        visited[temp] = 1
        result_bfs.append(temp)
        for n in nums[temp]:
            if (visited[n] == 0) and (n not in queue):
                queue.append(n)
    
    return result_bfs


queue = deque()
result_dfs = []
result_bfs = []

n, m, start = map(int, input().split())
nums = [[] for _ in range(n+1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    nums[x].append(y)
    nums[x] = list(set(nums[x]))
    nums[x].sort()
    nums[y].append(x)
    nums[y] = list(set(nums[y]))
    nums[y].sort()



ans_dfs = dfs(start)
visited = [0 for _ in range(n + 1)]
ans_bfs = bfs(start)

print(' '.join(map(str, ans_dfs)))
print(' '.join(map(str, ans_bfs)))

