def solution(rny_string):
    answer = ''
    for each in rny_string:
        if each == 'm':
            answer += 'rn'
        else:
            answer += each
    return answer