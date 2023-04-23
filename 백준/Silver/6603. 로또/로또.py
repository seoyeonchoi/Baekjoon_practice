def combi(level, start):  # 조합 함수
    if level == K:  # 조합 탈출 조건
        for a in arr: 
            print(a, end=' ') # 정답 원소들 하나씩 출력 
        print()  # 줄바꿈
        return
    
    for i in range(start, N-K+level+1):  # 각 레벨에서 고려해야 하는 만큼의 range 
        arr[level] = nums[i]  # 현재 레벨에서 고려한 단어 append
        combi(level+1, i+1)  # 그 다음 레벨 순회를 위한 재귀

while True:
    nums = list(map(int, input().split()))
    
    if nums[0] == 0:
        break
    else:
        N = nums[0]  # 고려해야하는 깊이
        K = 6  # 뽑을 수
        nums = nums[1:]
        answer_list = []
        arr = [0] * K
        combi(0, 0)
        print()