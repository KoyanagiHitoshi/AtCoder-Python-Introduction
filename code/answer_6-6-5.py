N = int(input())
dist = 100
for i in range(0, 101, 5):
    if abs(N-dist) > abs(N-i):
        dist = i
print(dist)
