import sys

input = sys.stdin.readline

G = int(input())

square_minus = []
calc = 3
while calc <= G:
    square_minus.append(calc)
    calc += 2

answer = []
start, end = 0, 0

while end <= len(square_minus):
    check = sum(square_minus[start:end])
    if check == G:
        answer.append(end)
        end += 1
    elif check < G:
        end += 1
    else:
        start += 1

if len(answer) == 0:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i] + 1)