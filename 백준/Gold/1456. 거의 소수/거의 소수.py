import sys
import math

if __name__ == "__main__":
    input = sys.stdin.readline
    a, b = map(int, input().split())

    check = [False,False] + [True]*(int(math.sqrt(b)) + 1)
    primes=[]

    answer = 0
    for i in range(2, int(math.sqrt(b)) + 1):
      if check[i]:
        cycle = 2
        while i**cycle <= b:
            if a <= i**cycle <=b:
                answer += 1
            cycle += 1
        for j in range(2*i, int(math.sqrt(b)) + 1, i):
            check[j] = False

    print(answer)

