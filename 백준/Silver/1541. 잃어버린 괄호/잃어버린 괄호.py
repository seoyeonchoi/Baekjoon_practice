calc = list(input())

new_calc = []
num = ''

# 문자열 -> 숫자식 전처리
for c in calc:
    if c == '+' or c == '-':
        new_calc.append(int(num))
        new_calc.append(c)
        num = ''
    else:
        num += c

new_calc.append(int(num))

stack = []
ans = new_calc[0]
for i in range(len(new_calc)):
    if new_calc[i] == '-':
        if len(stack) == 0:
            stack.append(new_calc[i+1])
        else:
            ans -= sum(stack)
            stack = []
            stack.append(new_calc[i+1])
    if new_calc[i] == '+':
        if len(stack) == 0:
            ans += new_calc[i+1]
        else:
            stack.append(new_calc[i+1])

ans -= sum(stack)

print(ans)
