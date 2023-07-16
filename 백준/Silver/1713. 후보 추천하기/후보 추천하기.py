from collections import defaultdict, deque

n = int(input())
m = int(input())
photos = dict()

recommend_list = deque((map(int, input().split())))

while recommend_list:
    ready = recommend_list.popleft()
    if ready in photos:
        photos[ready] += 1
    else:
        if len(photos) == n:
            keys = list(photos.keys())
            values = list(photos.values())
            min_val = values.index(min(values))
            idx = keys[min_val]
            del(photos[idx])
        
        photos[ready] = 1
        
print(" ".join(list(map(str, sorted(photos.keys())))))