N, M, X, T, D = map(int, input().split())
print(T if M >= X else T-(X-M)*D)
