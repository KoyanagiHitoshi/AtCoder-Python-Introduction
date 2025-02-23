N, L, R = map(int, input().split())
A = list(range(1, N+1))
A[L-1:R] = A[L-1:R][::-1]
print(*A)
