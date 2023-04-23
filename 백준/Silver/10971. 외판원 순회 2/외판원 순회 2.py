def perm(level):
    global ans
    if level >= N:
        current = get_cost(arr)
        # 계산된 값이 현재 최솟값보다 작으면 변경
        if current < ans:
            ans = current
        return
    
    for i in range(N):
        if visited[i]: continue
        
        visited[i] = 1
        arr[level] = nums[i]
        perm(level + 1)
        arr[level] = 0
        visited[i] = 0        
        
def get_cost(each_perm):
    # 각 순열 순회
    current = 0
    global ans
    for i in range(len(each_perm)):
        # 마지막 번호는 첫 번째 도시로 가는 길
        if (i == len(each_perm) - 1):
            if (costs[each_perm[i]][each_perm[0]] != 0):
                current += costs[each_perm[i]][each_perm[0]]
            else:
                current += ans
        # 아닌 경우는 다음 번호 도시로 가는 길
        elif (costs[each_perm[i]][each_perm[i+1]] != 0):
            current += costs[each_perm[i]][each_perm[i+1]]
        # else는 다음 도시로 갈 수 없는 경우를 의미 -> 그냥 현재 최소값으로 설정해서 값 변경이 일어나지 않도록 함
        else:
            current += ans
    # print(each_perm, current, ans)
    return current


N = int(input())
nums = [i for i in range(N)]
visited = [0] * N
arr = [0] * N

costs = []
# 가격 정보 리스트 생성
for i in range(N):
    each = list(map(int, input().split()))
    costs.append(each)

ans = 1000000*N # 최대 범위 가격 n개로 ans 설정
current = 0
perm(0)

print(ans)

# 처음에 순열을 다 리스트에 저장하고 각각의 가격을 구해 비교하니 메모리 초과 오류가 났다. 그래서 바로 고려하는 거로 바꿨다.
