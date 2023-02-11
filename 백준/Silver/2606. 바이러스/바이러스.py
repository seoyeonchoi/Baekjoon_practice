# 백준 2606 ver.2
from collections import deque

n = int(input())
link = int(input())
is_link = [[] for row in range(n)]
is_check = []
queue = deque()

for i in range(link):
    line = list(map(int, input().split()))
    is_link[line[0] - 1].append(line[1])
    is_link[line[1] - 1].append(line[0])

queue.append(1)
while len(queue) > 0:
    k = queue.popleft()
    if k not in is_check:
        is_check.append(k)
    for i in is_link[k-1]:
        if i not in is_check:
            queue.append(i)

print(len(is_check) - 1)