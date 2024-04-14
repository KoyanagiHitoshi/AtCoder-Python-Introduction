N, L = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for a in A:
    if a >= L:
        count += 1
print(count)
