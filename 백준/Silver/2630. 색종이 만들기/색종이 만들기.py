n = int(input())
papers = [ list(map(int, input().split())) for _ in range(n) ]
white = 0
blue = 0

def check_paper(width, height, size):
    global white
    global blue

    check = papers[width][height]
    for i in range(width, width + size):
        for j in range(height, height + size):
            if check != papers[i][j]:
                check = -1
                break
            
    if check == -1:
        size //= 2
        check_paper(width, height, size) # 왼쪽 위
        check_paper(width, height + size, size) # 오른쪽 위
        check_paper(width + size, height, size) # 왼쪽 아래
        check_paper(width + size, height + size, size) # 오른쪽 아래
    
    elif check == 1:
        blue += 1
    else:
        white += 1

check_paper(0, 0, n)
print(white)
print(blue)