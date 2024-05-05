A, B = map(int, input().split())
print(max(A+(A-1), B+(B-1), A+B))
