N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in range(M):
    total += A[B[i]-1]
print(total)
