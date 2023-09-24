import heapq

def solution(operations):
    heap = []
    for each in operations:
        # 삽입
        if each[0] == 'I':
            heapq.heappush(heap,  int(each[2:]))
        # 최솟값 삭제
        elif len(each) == 4:
            if heap:
                heapq.heappop(heap)
        # 최댓값 삭제
        else:
            if heap:
                heap.pop()

    answer = []
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
        
    return answer