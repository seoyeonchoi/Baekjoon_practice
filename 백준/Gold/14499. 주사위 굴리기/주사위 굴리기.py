import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
direction = list(map(int, input().split()))
dice = [0] * 6

cur_bottom = 5
cur_top = 0

# 좌표 이동
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def get_bottom_top(cur_d, cur_dice):
    if cur_d == 1:  # 동쪽 이동
        return [cur_dice[3], cur_dice[1], cur_dice[0], cur_dice[5], cur_dice[4], cur_dice[2]]
    elif cur_d == 2:  # 서쪽 이동
        return [cur_dice[2], cur_dice[1], cur_dice[5], cur_dice[0], cur_dice[4], cur_dice[3]]
    elif cur_d == 3:  # 북쪽 이동
        return [cur_dice[4], cur_dice[0], cur_dice[2], cur_dice[3], cur_dice[5], cur_dice[1]]
    elif cur_d == 4:  # 남쪽 이동
        return [cur_dice[1], cur_dice[5], cur_dice[2], cur_dice[3], cur_dice[0], cur_dice[4]]


for d in direction:
    # 현재 x를 기준으로 좌표값 갱신
    nx = x + dx[d]
    ny = y + dy[d]
    # print(d, nx, ny)
    # 범위 내의 이동이라면
    if 0 <= nx < n and 0 <= ny < m:
        dice = get_bottom_top(d, dice)
        # 밑 바닥 or 지도 갱신
        if board[nx][ny] == 0:
            board[nx][ny] = dice[cur_bottom]
        else:
            dice[cur_bottom] = board[nx][ny]
            board[nx][ny] = 0
        # print('현재 주사위: ', dice)
        # print('갱신된 board', board)

        # 현재 top 출력
        print(dice[cur_top])
        x = nx
        y = ny
