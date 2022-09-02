X, Y, N = map(int, input().split())
print(min(N*X, Y*(N//3)+X*(N % 3)))
