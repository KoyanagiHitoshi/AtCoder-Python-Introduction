N, C = map(int, input().split())
T = list(map(int, input().split()))
count = 1
before = T[0]
for t in T:
    if t-before >= C:
        count += 1
        before = t
print(count)
