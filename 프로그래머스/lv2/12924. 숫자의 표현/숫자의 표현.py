def solution(n):
    ans = 0
    end = 0
    start = 1
    answer = 0
    while(end <= n):
        # ans == n -> answer += 1 & ans += num+1
        if ans == n:
            answer += 1
            end += 1
            ans += end
        # ans > n -> ans -= start_num 
        elif ans > n: 
            ans -= start
            start += 1
        # ans < n -> ans += num+1
        else:
            end += 1
            ans += end
    return answer