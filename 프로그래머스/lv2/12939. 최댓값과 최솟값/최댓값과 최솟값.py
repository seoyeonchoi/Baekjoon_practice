def solution(s):
    num_list = list(map(int, s.split(' ')))
    num_list.sort()
    max_num = num_list[-1]
    min_num = num_list[0]
    answer = str(min_num) + ' ' + str(max_num)
    return answer