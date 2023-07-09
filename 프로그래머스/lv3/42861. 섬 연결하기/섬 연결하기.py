 # 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 값을 부모로 가지게 함
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    v, e = n, len(costs) # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    parent = [0] * (v + 1) # 부모 테이블 초기화하기
    answer = 0
    costs = sorted(costs, key = lambda x : (x[2]))
    
    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i
    
    # 간선 하나씩 확인
    for each in costs:
        a, b, cost = each
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer