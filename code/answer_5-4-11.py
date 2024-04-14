N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for b in B:
    total += A[b-1]
print(total)
