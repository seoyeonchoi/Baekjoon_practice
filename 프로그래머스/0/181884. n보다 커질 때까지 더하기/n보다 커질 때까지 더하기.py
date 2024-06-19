def solution(numbers, n):
    answer = 0
    for each in numbers:
        if answer > n:
            return answer
        else:
            answer += each
    return answer