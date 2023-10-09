import sys

input = sys.stdin.readline

def Find(x):
    if x != parents[x]:
        parents[x] = Find(parents[x])

    return parents[x]


def Union(a, b):
    a = Find(a)
    b = Find(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    Union(a, b)

schedule = list(map(int, input().split()))
ans = 0
for i in range(1, len(schedule)):
    if Find(schedule[i-1]) != Find(schedule[i]):
        ans += 1

print(ans)