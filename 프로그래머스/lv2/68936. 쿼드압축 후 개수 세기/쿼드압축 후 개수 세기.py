def solution(arr):
    result = [0,0]
    size = len(arr)
    # cnt1 = 0
    # cnt0 = 0

    def quadtree(width, height, size):

        check = arr[width][height]
        for i in range(width, width + size):
            for j in range(height, height + size):
                if check != arr[i][j]:
                    check = -1
                    break

        if check == -1:
            size //= 2
            quadtree(width, height, size) # 왼쪽 위
            quadtree(width, height + size, size) # 오른쪽 위
            quadtree(width + size, height, size) # 왼쪽 아래
            quadtree(width + size, height + size, size) # 오른쪽 아래


        elif check == 1:
            # cnt1 += 1
            result[1] += 1
        else:
            # cnt0 += 1
            result[0] += 1
        
    quadtree(0, 0, size)
    # answer = [cnt0, cnt1]
    print(result)
    # print(cnt1, cnt0)
    
    # return answer
    return result