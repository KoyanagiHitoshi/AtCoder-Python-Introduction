N, K = map(int, input().split())
A = list(map(int, input().split()))
print(*A[-K:]+A[:N-K])
