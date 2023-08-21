import math
import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
team_min = math.inf
visited = [False] * n


def dfs(depth, idx):
    global team_min
    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += board[i][j]
                elif not visited[i] and not visited[j]:
                    link += board[i][j]
        team_min = min(team_min, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

            
dfs(0, 0)
print(team_min)