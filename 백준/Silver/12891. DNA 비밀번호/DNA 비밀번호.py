import sys
from collections import Counter

input = sys.stdin.readline

S, P = map(int, input().split())
dna = list(input().rstrip())
a, c, g, t = map(int, input().split())

min_cnt = {'A': a, 'C': c, 'G': g, 'T': t}
cur_cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

cnt = 0

for i in range(S - P + 1):
    if i > 0:
        cur_cnt[dna[i + P - 1]] += 1
        cur_cnt[dna[i - 1]] -= 1
    else:
        for k, v in Counter(dna[:P]).items():
            cur_cnt[k] = v

    is_ok = 0
    for x in ['A', 'C', 'G', 'T']:
        if min_cnt[x] > cur_cnt[x]:
            is_ok = 1
            break

    if is_ok == 0: cnt += 1

print(cnt)