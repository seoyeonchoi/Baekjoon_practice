from collections import deque

def solution(s):
    queue = deque(s)


    def check_bracket(array):
        stack = []
        for a in array:
            if a == '(' or a == '[' or a == '{':
                stack.append(a)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == '(' and a == ')':
                        stack.pop()
                    elif stack[-1] == '{' and a == '}':
                        stack.pop()
                    elif stack[-1] == '[' and a == ']':
                        stack.pop()
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False


    cnt = 0
    for _ in range(len(queue)):
        result = check_bracket(queue)
        if result:
            cnt += 1
        queue.append(queue.popleft())

    return cnt