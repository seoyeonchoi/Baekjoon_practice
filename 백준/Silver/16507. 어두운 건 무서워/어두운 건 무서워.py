import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
pixels = [[0 for _ in range(c+1)]]

for _ in range(r):
    pixels.append([0] + list(map(int, input().split())))

sum_pixels = [[0 for _ in range(c+1)] for _ in range(r+1)]

for i in range(1, r+1):
    temp = 0
    for j in range(1, c+1):
        temp += pixels[i][j]
        sum_pixels[i][j] = temp
        
for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    div_num = (c2 - c1 + 1) * (r2 - r1 + 1)
    ans = 0        
    for i in range(r1, r2+1):
        ans += sum_pixels[i][c2] - sum_pixels[i][c1-1]
    print(ans // div_num)