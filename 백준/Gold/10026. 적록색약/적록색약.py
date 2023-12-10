import sys
from collections import deque

def solution():
    n = int(input())
    paints = []
    for _ in range(n):
        paints.append(list(input().rstrip()))
    paints_rg = paints.copy()

    # 상, 하, 좌, 우 탐색을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * n for _ in range(n)]

    def bfs(x, y, visited, grid, target):
        queue = deque([(x, y)])
        # 현재 위치를 방문했다고 표시
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            # 현재 위치에서 인접한 위치 탐색
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                # 배열 범위 안에 있고 방문하지 않았다면 큐에 넣고 탐색
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] in target:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    grid = {'R': 0, 'G': 0, 'B': 0}
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                grid[paints[i][j]] += 1
                bfs(i, j, visited, paints, [paints[i][j]])

    visited = [[False] * n for _ in range(n)]
    grid2 = {1: 0, 2: 0}
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if paints[i][j] in ['R', 'G']:
                    grid2[1] += 1
                    bfs(i, j, visited, paints, ['R', 'G'])
                else:
                    grid2[2] += 1
                    bfs(i, j, visited, paints, [paints[i][j]])

    print(sum(grid.values()), sum(grid2.values()))


if __name__ == "__main__":
    input = sys.stdin.readline
    solution()