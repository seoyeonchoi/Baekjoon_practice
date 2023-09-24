import sys

input = sys.stdin.readline

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(input().rstrip()))


def dfs_stack(x, y, visited):
    stack = [(x, y)]
    # 현재 위치를 방문했다고 표시
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()

        # 현재 위치에서 인접한 위치 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 배열 범위 안에 있고 방문하지 않았다면 스택에 넣고 탐색
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == '0':
                if nx == m-1:
                    return True
                else:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

    return False


# 방문 정보
visited = [[False] * n for _ in range(m)]
result = False

for j in range(n):
    if board[0][j] == '0':
        result = dfs_stack(0, j, visited)
        if result:
            break

print('YES' if result else 'NO')