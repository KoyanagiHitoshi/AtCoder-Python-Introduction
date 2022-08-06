A, B, C, K = map(int, input().split())
print(min(K, A)-max(0, K-A-B))
