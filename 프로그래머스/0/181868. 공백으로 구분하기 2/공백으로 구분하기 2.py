def solution(my_string):
    origin = my_string.split(' ')
    answer = []
    for each in origin:
        if each != '':
            answer.append(each)
    return answer