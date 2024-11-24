A = list(map(int, input().split()))
color = [0, 0, 0, 0]
for a in A:
    color[a-1] += 1
count = 0
for num in color:
    if num == 4:
        count += 2
    elif num in [2, 3]:
        count += 1
print(count)
