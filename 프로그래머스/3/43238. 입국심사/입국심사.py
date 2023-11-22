def solution(n, times):
    
    # left = 0초, right = 빨리 처리할 수 있는 한 사람이 모든 사람을 감당할 때 걸리는 시간
    left, right = 0, min(times) * n
    
    while left <= right:
        # 모든 사람이 심사를 받는데 걸리는 시간을 mid로 관리
        mid = (left + right) // 2
        
        check = 0
        
        for each in times:
            check += (mid // each)  # 총 시간 동안 한 사람(each)이 검사하는 사람 수
        
        # n보다 작으면 총 시간 더 필요
        if check < n:
            left = mid + 1
        # n보다 크면 총 시간 덜 필요
        else:
            right = mid - 1
    
    # 최솟값을 구해야 하므로 left 반환
    return left