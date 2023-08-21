import itertools

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    nums = list(numbers)

    prime_set = set()

    for length in range(1, len(nums) + 1):
        perm = itertools.permutations(nums, length)
        for p in perm:
            num = int(''.join(p))
            if check_prime(num) and num not in prime_set:
                prime_set.add(num)
                answer += 1
    return answer