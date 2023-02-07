n = int(input())
cnt = 0

if n%5 == 0:
    cnt = n//5
elif n%5 == 1:
    cnt = (n-6)//5+2
elif (n%5 == 2) and (n>7):
    cnt = (n-12)//5+4
elif n%5==3:
    cnt = (n-3)//5+1
elif (n%5==4) and (n>4):
    cnt = (n-9)//5+3
else:
    cnt=-1

print(cnt)