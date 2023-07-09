import sys

# Input = sys.stdin.readline()
n, k = map(int, input().split())
members = list(map(int, input().split()))
member_minus = []

for i in range(n-1):
    member_minus.append(members[i+1] - members[i])

member_minus.sort()

for i in range(k-1):
    member_minus.pop()
    
print(sum(member_minus))