def solution(my_string, alp):
    answer = ''
    for each in my_string:
        if each == alp:
            answer += alp.upper()
        else:
            answer += each
    return answer