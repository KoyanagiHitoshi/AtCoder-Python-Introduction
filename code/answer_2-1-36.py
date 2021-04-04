N, X, T = map(int, input().split())
print(T*(N//X) if N % X == 0 else T*(N//X+1))
