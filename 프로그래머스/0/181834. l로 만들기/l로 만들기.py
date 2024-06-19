def solution(myString):
    answer = ''
    for each in myString:
        if ord(each) < ord('l'):
            answer += 'l'
        else:
            answer += each
    return answer