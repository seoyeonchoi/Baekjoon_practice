# 2002

N = int(input())
start = []
end = []

for i in range(N):
    each = input()
    start.append(each)

for i in range(N):
    each = input()
    end.append(each)
    
check = 0

for i in range(N):
    
    s_idx = start.index(start[i])
    e_idx = end.index(start[i])
    
    s_front = start[:s_idx]
    e_front = end[:e_idx]
    
    for s in s_front:
        if s in e_front:
            continue
        else:
            check += 1
            break
    
print(check)
    