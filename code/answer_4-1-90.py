A, B, C = map(int, input().split())
if (B < C and not B < A < C) or (C < B and C < A < B):
    print("Yes")
else:
    print("No")
