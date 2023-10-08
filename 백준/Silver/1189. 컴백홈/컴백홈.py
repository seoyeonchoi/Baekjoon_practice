import sys
from collections import deque

input = sys.stdin.readline

n, c, k = map(int, input().split())
board = []
visited = [[False for _ in range(c)] for _ in range(n)]
for _ in range(n):
    board.append(list(input().rstrip()))

ans = 0


def backtracking(x, y, cnt):
    global ans
    if x == 0 and y == c-1:
        if cnt == k:
            ans += 1
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < c:
            if not visited[nx][ny] and board[nx][ny] == '.':
                visited[nx][ny] = True
                backtracking(nx, ny, cnt + 1)
                visited[nx][ny] = False


visited[n-1][0] = True
backtracking(n-1, 0, 1)
print(ans)
