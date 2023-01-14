# 1110
ori_num = int(input())
cycle = 0
num = ori_num
while (True):
    cycle += 1
    # 10보다 작으면 앞에 0을 붙여 두 자리수로 만든다
    if num<10:
        sum_num = num
    # 각 자리 숫자를 더한다
    else:
        sum_num = num//10 + num%10
    # 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙여 새로운 수를 만든다.
    new_num = (num%10)*10 + sum_num%10
    # 원래 숫자로 돌아오기까지의 사이클을 구한다.
    if new_num == ori_num:
        break
    else:
        num = new_num
        
print(cycle)