import sys
import heapq

input = sys.stdin.readline

plus_heap = []  # 양수 저장 heap
minus_heap = []  # 음수 저장 heap

T = int(input())
for _ in range(T):
    check = int(input())
    # 출력 해야 하는 경우
    if check == 0:
        # 두 heap 모두 입력 값이 있는 경우
        if len(plus_heap) > 0 and len(minus_heap) > 0:
            # 양수의 절댓값이 더 작은 경우
            if plus_heap[0] < minus_heap[0]:
                print(heapq.heappop(plus_heap))
            else:
                # 두 절댓값이 같거나, 음수의 절댓값이 더 작은 경우
                print(-heapq.heappop(minus_heap))
        # 음수에만 저장된 수가 있는 경우
        elif len(plus_heap) == 0 and len(minus_heap) > 0:
            print(-heapq.heappop(minus_heap))
        # 양수에만 저장된 수가 있는 경우
        elif len(plus_heap) > 0 and len(minus_heap) == 0:
            print(heapq.heappop(plus_heap))
        # 두 수 모두 저장된 수가 없는 경우
        elif len(plus_heap) == 0 and len(minus_heap) == 0:
            print(0)
    # 입력 해야 하는 경우
    else:
        if check < 0:
            # 음수면 -를 제외하고 저장해서 절댓값 기준 최소힙으로 저장. 이후 heappop 과정에서 다시 -붙임
            heapq.heappush(minus_heap, -check)
        else:
            heapq.heappush(plus_heap, check)