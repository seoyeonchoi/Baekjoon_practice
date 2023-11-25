import sys

def solution(coin, cards):
    answer = 0
    for idx, m in enumerate(mountains[:n-1]):
        answer += abs(m - mountains[idx+1])**2 + (m + mountains[idx+1])**2
    print(answer)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    mountains = list(map(int, input().split()))
    solution(n, mountains)