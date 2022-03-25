N, A, X, Y = map(int, input().split())
print(N*X-max(N-A, 0)*(X-Y))
