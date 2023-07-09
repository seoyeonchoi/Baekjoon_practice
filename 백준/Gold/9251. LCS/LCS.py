# 상향식 버전
def lcs(x, y):
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)] # dp
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]: 
                c[i][j] = c[i - 1][j - 1] + 1 # 끝이 같을 때 
            else: 
                c[i][j] = max(c[i][j - 1], c[i - 1][j]) # 끝이 다를 때
    return c[m-1][n-1]

 
s1 = list(input())
s2 = list(input())
ans = lcs(s1, s2)
print(ans)