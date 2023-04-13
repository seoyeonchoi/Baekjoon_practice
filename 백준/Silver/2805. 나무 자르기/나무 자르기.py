# 2805
import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
mid = (start + end)//2  # 이진 탐색을 위한 중간점 지정

while (start < end) and (start != mid) and (end != mid):
    total = 0
    for tree in trees:  # mid 값보다 큰 나무는의 차이를 total 변수에 저장
        if tree > mid:
            total += (tree-mid)
    if total == m:
        break
    elif total > m:  # total이 원하는 나무 길이보다 큰 경우 나무를 덜 잘라야 하므로(=mid가 커져야 함) start 이동
        start = mid
    else:  # total이 원하는 나무 길이보다 짧은 경우 나무를 더 잘라야 하므로(=mid가 작아져야 함) end 이동
        end = mid
    mid = (start + end)//2  # 이진 탐색을 위한 중간점 지정

print(mid)
