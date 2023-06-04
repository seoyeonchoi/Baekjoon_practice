import sys

n, k, q, m = map(int, sys.stdin.readline().split())
sleep = list(map(int, sys.stdin.readline().split()))
check_start = list(map(int, sys.stdin.readline().split()))

idx_check = [ i for i in range(3, n+3)]
attend = [0 for _ in range(n)]

for each in check_start:
    i = 1
    if each not in sleep:
        while each * i - 3 <= n - 1:
            attend[each * i - 3] = 1
            i += 1

for each in sleep:
    if attend[each - 3] == 1:
        attend[each - 3] = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    ans = 0
    for idx, each in enumerate(attend):
        if (s <= idx_check[idx] <= e) and (each == 0):
            ans += 1

    print(ans)