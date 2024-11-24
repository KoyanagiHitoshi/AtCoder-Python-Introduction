X, Y, Z = map(int, input().split())
A, B, C = X, Y, Z
A, B = B, A
A, C = C, A
print(A, B, C)
