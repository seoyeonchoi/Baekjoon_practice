def solution(n):
    answer = 0
    
    n_one = bin(n).count('1')
    
    for i in range(n+1, 1000001):
        i_one = bin(i).count('1')
        if n_one == i_one:
            answer = i
            break
            
    return answer