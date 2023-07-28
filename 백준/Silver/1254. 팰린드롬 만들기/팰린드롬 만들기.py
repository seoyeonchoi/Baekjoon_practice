import sys

input = sys.stdin.readline

words = list(input().rstrip())
words_rv = words.copy()
words_rv.reverse()

for i in range(1, len(words) + 1):
    # 문자 자체가 팰린드롬인 경우
    if words == words[::-1]:
        new_w = words
        break
    # 그 외
    new_w = words + words_rv[-i:]
    if new_w == new_w[::-1]:
        break

print(len(new_w))