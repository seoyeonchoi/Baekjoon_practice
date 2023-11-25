import sys

def solution(n, missions):
    times = [0 for _ in range(240000)]
    for mission in missions:
        a, b, c = mission
        if a == 1:
            for i in range(b, c):
                if (i % 100) < 60 and (i % 10000) < 6000:  # 시간, 분 처리
                    times[i] += 1
        elif a == 2:
            print(sum(times[b:c]))

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    missions = []
    for _ in range(n):
        a, b, c = list(input().split())
        missions.append([int(a), int(b.replace(':', '')), int(c.replace(':', ''))])
    solution(n, missions)