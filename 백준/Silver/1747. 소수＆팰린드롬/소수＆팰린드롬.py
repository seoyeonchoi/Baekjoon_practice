import math

def divide_check(n):
    div_num = 2
    while(div_num < int(math.sqrt(n)+1)):
        if n % div_num:
            div_num += 1
        else:
            return 0
    return 1
            
def palin_check(n):
    check = str(n)
    if str(n) == check[::-1]:
        return 1
    else: return 0

n = int(input())

while (True):
    if n == 1:
        print(2)
        break
    elif (divide_check(n) == 1) and (palin_check(n) == 1):
        print(n)
        break
    else:
        n += 1
