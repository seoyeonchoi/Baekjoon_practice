# 아이디어
# 끝 글자 스택 -> 뒷 글자 pop -> 안 같으면 break
# word in word[:지금까지] -> 있으면 break
# break 했을 때 len%n

def solution(n, words):
    answer = []
    stack = [words[0][-1]]
    cnt = 2 # 첫 번째는 오류가 날 수 없고(시작이어서) 두 번째 단어부터 검증
    isError = False
    
    for word in words[1:]:
        if stack[-1] != word[0]:
            isError = True
            break
        elif words[:cnt].count(word) > 1:
            isError = True
            break
        else:
            stack.append(word[-1])
            cnt += 1
            
    print(cnt) # 문제 발생한 부분의 index
    print(isError) # 에러 여부
    
    if isError == False:
        answer = [0,0]
    else:
        num = n if (cnt)%n == 0 else (cnt)%n
        turn = (cnt)//n if (cnt)%n == 0 else (cnt//n)+1
        answer = [num, turn] 
    
    return answer