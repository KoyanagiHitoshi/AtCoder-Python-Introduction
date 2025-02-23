N, X, T = map(int, input().split())
if N % X == 0:
    print(T*(N//X))
else:
    print(T*(N//X+1))
