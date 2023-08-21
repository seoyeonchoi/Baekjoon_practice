import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a_list = list(map(str, str(a)))
a_list.sort(reverse=True)

visited = [False] * len(a_list)
max_a = 0


def backtracking(check):
    global max_a

    if len(check) == len(a_list) and int(check) < b:
        if check[0] != '0':
            max_a = max(max_a, int(check))

    for i in range(len(a_list)):
        if not visited[i]:
            visited[i] = True
            backtracking(check + a_list[i])
            visited[i] = False


backtracking('')
if max_a > 0:
    print(max_a)
else:
    print(-1)