X, Y, N = map(int, input().split())
if X < Y/3:
    print(X*N)
else:
    print(Y*(N//3)+X*(N % 3))
