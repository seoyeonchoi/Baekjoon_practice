from collections import deque

n, s, m = map(int, input().split())
v_list = list(map(int, input().split()))

check_queue = deque()
check_queue.append(s)

for v in v_list:

    now = deque([])
    for _ in range(len(check_queue)):
        check = check_queue.popleft()

        if 0 <= check + v <= m:
            if check + v not in now:
                now.append(check + v)
        if 0 <= check - v <= m:
            if check - v not in now:
                now.append(check - v)
                
    check_queue = now
    if len(check_queue) <= 0:
        break

if len(check_queue) > 0:
    print(max(check_queue))
else:
    print(-1)