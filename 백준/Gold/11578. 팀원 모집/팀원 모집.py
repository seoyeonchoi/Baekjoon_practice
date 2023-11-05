import sys
import math


def backtracking(solved, each):
    global ans
    if each > ans:
        return
    elif all(solved[1:]):
        ans = each
        return

    for i in range(number_of_students):
        if not visited[i]:
            origin_solved = solved.copy()
            for j in students[i]:
                solved[j] = True
            visited[i] = True
            backtracking(solved, each+1)
            visited[i] = False
            solved = origin_solved.copy()



if __name__ == "__main__":
    input = sys.stdin.readline
    number_of_questions, number_of_students = map(int, input().split())
    students = []
    solved = [False] * (number_of_questions + 1)
    visited = [False] * number_of_students
    ans = math.inf

    for _ in range(number_of_students):
        students.append(list(map(int, input().split()))[1:])
    students.sort(key=len, reverse=True)
    backtracking(solved, 0)
    print(-1 if ans == math.inf else ans)