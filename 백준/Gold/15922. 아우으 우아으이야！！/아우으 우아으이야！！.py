import sys

input = sys.stdin.readline

lines = []
n = int(input())
for _ in range(n):
    lines.append(list(map(int, input().split())))

ans = 0
save_start, save_end = lines[0][0], lines[0][1]
i = 1
if n == 1:
    ans += (save_end - save_start)
    print(ans)
else:
    while i < n:
        # 이어져 있는 경우 갱신
        if lines[i][0] < save_end:
            save_end = max(save_end, lines[i][1])
        else:
            # 끊어진 경우 계산 후 갱신
            ans += (save_end - save_start)
            save_start = lines[i][0]
            save_end = lines[i][1]

        # 마지막 갱신
        if i == n-1:
            ans += (save_end - save_start)

        i += 1

    print(ans)
