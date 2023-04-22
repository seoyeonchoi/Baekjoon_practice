def nCr(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)
    
while True:
    nums = list(map(int, input().split()))
    answer_list = []
    
    if nums[0] == 0:
        break
    else:
        nCr(1, [], 6)
        for answer in answer_list:
            for a in answer:
                print(a, end=' ')
            print()
        print()