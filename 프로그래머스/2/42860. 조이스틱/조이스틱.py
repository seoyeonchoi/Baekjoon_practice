from collections import deque

def solution(name):
    is_checked = [False for _ in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            is_checked[i] = True
    queue = deque([])
    queue.append((0, is_checked, 0))
    
    if name.count('A') == len(name):
        return 0
    
    while queue:
        idx, each_checked, ans = queue.popleft()
        if not each_checked[idx]:
            each_checked[idx] = True
            ans += min((ord(name[idx]) - ord('A')), (ord('Z') - ord(name[idx]) + 1))
        if all(each_checked):
            return ans
        else:
            queue.append((idx + 1, each_checked.copy(), ans + 1))
            queue.append((idx - 1, each_checked.copy(), ans + 1))
        
    return ans