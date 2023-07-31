import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 길이가 m인 숫자 조합
perm = list(combinations(nums, m))
ans = [] 

# 중복 체크 및 오름차순 정렬
for i in range(len(perm)):
    perm[i] = sorted(list(perm[i]))
    if perm[i] not in ans:
        ans.append(perm[i])

# 정렬
ans = sorted(ans)

# 출력
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=' ')
    print()
