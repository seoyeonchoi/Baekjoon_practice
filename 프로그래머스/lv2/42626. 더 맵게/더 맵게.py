import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    if scoville[0] >= K:
        return answer
    else:
        while scoville[0] < K:
            if len(scoville) < 2:
                return -1
            else:
                min_sco = heapq.heappop(scoville)
                min_sco2 = heapq.heappop(scoville)

                heapq.heappush(scoville, min_sco + (min_sco2 * 2) )
                answer += 1

        return answer