num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
if (num_list[0] == num_list[1]) & (num_list[1]==num_list[2]):
    print(10000+num_list[0]*1000)
elif (num_list[0] == num_list[1]) | (num_list[1]==num_list[2]):
    print(1000+num_list[1]*100)
else:
    print(num_list[0]*100)