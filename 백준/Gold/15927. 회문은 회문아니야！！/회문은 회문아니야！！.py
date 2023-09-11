import sys

input = sys.stdin.readline

def not_palin(array):
    if len(set(array)) == 1:
        return -1
    elif array != array[::-1]:
        return len(array)
    else:
        return len(array) - 1

check = list(input().rstrip())
result = not_palin(check)

if result == -1:
    print(-1)
else:
    print(result)
