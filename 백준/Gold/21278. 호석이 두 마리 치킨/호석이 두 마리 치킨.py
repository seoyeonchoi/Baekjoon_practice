import itertools
import math
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

    # 연결 정보 입력
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    # 자기자신 초기화
    for i in range(1, n+1):
        graph[i][i] = 0

    # 플로이드 워셜 점화식
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 두 개 뽑는 조합
    combis = itertools.combinations([i for i in range(1, n+1)], 2)

    answer = math.inf
    answer_combi = (0, 0)
    for combi in combis:
        each_ans = 0
        for i in range(1, n+1):
            if i not in combi:
                each_ans += min(graph[i][combi[0]], graph[i][combi[1]]) * 2
        if each_ans < answer:
            answer = each_ans
            answer_combi = combi

    print(answer_combi[0], answer_combi[1], answer)
