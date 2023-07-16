from collections import Counter

def solution(k, tangerine):
    
    counter_tangerine = Counter(tangerine)
    counter_tangerine_values = list(counter_tangerine.values())
    counter_tangerine_values.sort(reverse=True)
    
    answer = 0
    ans = 0
    
    while ans < k :
        ans += counter_tangerine_values[answer]
        answer += 1

    return answer