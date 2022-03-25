A, B, C, X = map(int, input().split())
print(1 if X <= A else 0 if X > B else C/(B-A))
