import sys

input = sys.stdin.readline

n, length = map(int, input().split())
water = list(map(int, input().split()))
water.sort()

start = water[0] - 0.5
end = start + length
cnt = 1
for w in water[1:]:
    if w < end:
        continue
    else:
        start = w - 0.5
        end = start + length
        cnt += 1

print(cnt)