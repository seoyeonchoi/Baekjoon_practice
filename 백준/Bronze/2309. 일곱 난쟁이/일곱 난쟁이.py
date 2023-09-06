import itertools
import sys

input = sys.stdin.readline

check = []
for _ in range(9):
    check.append(int(input()))

for c in itertools.combinations(check, 7):
    if sum(c) == 100:
        ans = list(c)
        ans.sort()
        for a in ans:
            print(a)
        break