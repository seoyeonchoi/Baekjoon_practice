# def solution(s):
#     # 전체를 lower로 바꿈, 공백 단위로 리스트화
#     s_list = s.split(' ')
#     answer = ''
#     for s_item in s_list:
#         if (len(s_item) > 0):
#             answer += s_item[0].upper() + s_item[1:].lower() + ' '
#     return answer[:-1]

def solution(s):
    answer =''
    for i in s.split(' '):
        i = i.lower()
        i = i.capitalize()
        answer += i +' '
    return answer[:-1]