N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
distance = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        distance = max(distance, ((x1-x2)**2+(y1-y2)**2)**0.5)
print(distance)
