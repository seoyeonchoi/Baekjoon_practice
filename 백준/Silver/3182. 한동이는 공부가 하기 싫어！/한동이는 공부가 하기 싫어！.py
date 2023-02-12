n = int(input())
num_list = []

for _ in range(n):
    k = int(input())
    num_list.append(k)
    
max_cnt = 0
answer = 1

for i in range(len(num_list)):
    is_check=[0]*n
    is_check[i] = 1
    check = num_list[i]
    cnt = 1
    while(cnt<=n):
        if is_check[check-1] == 0:
            is_check[check-1] = 1
            cnt += 1
            check = num_list[check-1]
        else:
            break
            
    if cnt > max_cnt:
        max_cnt = cnt
        answer = i+1

print(answer)