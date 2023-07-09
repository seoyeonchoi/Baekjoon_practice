from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) # pop(0)의 시간 복잡도를 줄이기 위해 얘도 deque로 바꿈
    bridge = deque([0 for _ in range(bridge_length)])
    answer = 0
    sum_bridge = 0
    
    while truck_weights:
        sum_bridge -= bridge.popleft()
        
        if sum_bridge + truck_weights[0] > weight:
            bridge.append(0)
        else:
            ready = truck_weights.popleft()
            bridge.append(ready)
            sum_bridge += ready
            
        answer += 1
    
    # print(answer, bridge)
    answer += bridge_length
        
    return answer