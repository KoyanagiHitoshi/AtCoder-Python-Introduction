V, A, B, C = map(int, input().split())
V = V % (A+B+C)
print("F" if V-A < 0 else "M" if V-(A+B) < 0 else "T")
