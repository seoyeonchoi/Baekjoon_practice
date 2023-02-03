def solution(arr):
    answer = 0
    maximum = arr[0]
    multi = 1
    
    for a in arr:
        if a > maximum:
            maximum = a
        multi *= a
    
    print(maximum, multi)
    
    for i in range(maximum, multi+1):
        isAnswer = 0
        for a in arr:
            if i%a:
                isAnswer = 1
                break
        if isAnswer == 0:
            answer = i
            break
    
    return answer