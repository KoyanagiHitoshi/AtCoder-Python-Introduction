N, M = map(int, input().split())
A = list(map(int, input().split()))
print(N-sum(A) if N-sum(A) >= 0 else -1)
