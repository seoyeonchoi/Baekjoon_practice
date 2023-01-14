# 4344
case = int(input())
for i in range(case):
    each_case = list(map(int, input().split()))
    mean = (sum(each_case) - each_case[0]) /each_case[0]
    cnt = 0
    for each in each_case[1:]:
        if each > mean:
            cnt += 1
    result = cnt / each_case[0] * 100
    print(f"{result:.3f}%")