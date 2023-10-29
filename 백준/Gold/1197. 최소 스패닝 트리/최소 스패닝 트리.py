import sys
# 무방향 가중치 그래프에서 간선의 가중치 합이 최소인 트리(=최소신장트리)의 가중치 구하기
# 크루스칼 알고리즘: 간선들의 가중치가 작은 것부터 오른차순 정렬 후 사이클 이루지 않는 트리 간선 선택

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parents[b] = a
    else:
        parents[a] = b
        # if rank[a] == rank[b]:
        #     rank[b] += 1


def solution(n, m, edges, parents):
    answer = 0
    for i in range(1, n+1):
        parents[i] = i
    for i in range(m):
        node1, node2, cost = map(int, input().split())
        edges.append((cost, node1, node2))
    # 가중치 기준 오름차순 정렬
    edges.sort()

    for edge in edges:
        cost, node1, node2 = edge
        # 두 노드의 루트 노드가 다르다면(= 두 노드 떨어져 있다면)
        if find(node1) != find(node2):
            # 두 노드 합쳐주기
            union(node1, node2)
            # 합친 후의 가중치 더해주기
            answer += cost
    return answer



if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    parents = {}
    answer = 0
    print(solution(n, m, edges, parents))

