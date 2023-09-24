import sys

input = sys.stdin.readline


def prime_factorization(n):
    i = 2
    ans_list = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            ans_list.append(i)
    if n > 1:
        ans_list.append(n)

    return ans_list


num = int(input())
answer = prime_factorization(num)
print(len(answer))
for a in answer:
    print(a, end=' ')