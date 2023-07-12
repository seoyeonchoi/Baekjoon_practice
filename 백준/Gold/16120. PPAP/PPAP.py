origin = list(input())
stack = []

for o in origin:
    stack.append(o)
    if (len(stack) >= 4) and (stack[-4:] == ['P', 'P', 'A', 'P']):
        stack[-4:] = ['P']

if stack == ['P']:
    print('PPAP')
else:
    print('NP')