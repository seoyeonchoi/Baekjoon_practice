import sys, math
from itertools import combinations

input = sys.stdin.readline

# 입력
n = int(input())
players = [ list(map(int, input().split())) + [i] for i in range(1, n + 1)]

# 승리 횟수 저장 딕셔너리 초기화
victory_dict = {}
for i in range(1, n + 1):
    victory_dict[i] = 0

# 게임 조합 별 승리 회수 저징
for player1, player2 in combinations(players, 2):
    p1_power = player1[0] + player1[1] * player2[0]
    p2_power = player2[0] + player2[1] * player1[0]
    if p1_power > p2_power:
        victory_dict[player1[2]] += 1
    else:
        victory_dict[player2[2]] += 1

answer = sorted(victory_dict, key=lambda x: victory_dict[x], reverse=True)
for a in answer:
    print(a)