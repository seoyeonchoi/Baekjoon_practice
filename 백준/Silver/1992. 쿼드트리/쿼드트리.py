n = int(input())
array = [ list(map(int, input())) for _ in range(n) ]

def quadtree(width, height, size):
    check = array[width][height]
    for i in range(width, width + size):
        for j in range(height, height + size):
            if check != array[i][j]:
                check = -1
                break
            
    if check == -1:
        print('(', end='')
        size //= 2
        quadtree(width, height, size) # 왼쪽 위
        quadtree(width, height + size, size) # 오른쪽 위
        quadtree(width + size, height, size) # 왼쪽 아래
        quadtree(width + size, height + size, size) # 오른쪽 아래
        print(')', end='')

    
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

quadtree(0, 0, n)