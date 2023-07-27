import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
ans = [0] * n

for j in range(1, n+1):
    i = 0
    pass_i = 0
    while True:
        # 해당 자리에 이미 저장된 값이 있으면 패스
        if ans[i + pass_i] != 0:
            pass_i += 1
        # 아직 i값이 올 자리가 아니면 += 1
        elif i != nums[j]:
            i += 1
        # 자리를 찾으면 값 입력
        elif i == nums[j]:
            ans[i + pass_i] = j
            break

for a in ans:
    print(a, end=' ')
