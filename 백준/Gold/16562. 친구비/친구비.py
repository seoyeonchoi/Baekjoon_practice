import sys
from collections import deque

def solution(friends, money, n, m, k):
    is_friend = [False for _ in range(n+1)]
    answer = 0
    for f in range(1, n+1):
        if not is_friend[f]:
            is_friend[f] = True
            queue = deque([f])
            min_each = money[f]
            while queue:
                nxt = queue.popleft()
                for each in friends[nxt]:
                    if not is_friend[each]:
                        is_friend[each] = True
                        queue.append(each)
                        min_each = min(min_each, money[each])
            answer += min_each

    for check in range(1, n+1):
        if not is_friend[check]:
            answer += money[check]
            
    if answer <= k:
        print(answer)
    else:
        print('Oh no')

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    money = [0] + list(map(int, input().split()))
    friends = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    solution(friends, money, n, m, k)