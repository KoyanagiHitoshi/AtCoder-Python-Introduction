N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(K, X)
print(*A)
