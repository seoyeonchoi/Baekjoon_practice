def solution(s):
    circle = 1
    zero_cnt = 0
    while(True):
        zero_in_circle = 0
        # 문자열에서 0을 전부 제거
        for s_item in s:
            if s_item == '0':
                zero_in_circle += 1                
        # 0 제거 후 남은 문자열의 길이를 이진 변환
        next_s = len(s) - zero_in_circle
        s = str(bin(next_s))[2:] # 이진수를 의미하는 앞 '0b' 제거 위함
        zero_cnt += zero_in_circle
        if s == '1':
            break
        # while문 cnt +1, 제거한 0 개수 +
        else:
            circle += 1
    # 최종 결과 리스트 반환
    answer = [circle, zero_cnt]
    return answer