n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if k >= n: 
    print(0)
else:
    sensor_minus = []
    for i in range(len(sensor) - 1):
        tmp = sensor[i+1] - sensor[i]
        sensor_minus.append(tmp)
        
    sensor_minus.sort(reverse=True)
        
    for _ in range(k-1):
        sensor_minus.pop(0)

    print(sum(sensor_minus))