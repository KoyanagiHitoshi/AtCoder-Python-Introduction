A, B, C, D = map(int, input().split())
if (C < A) or (C == A and D < B):
    print("Yes")
else:
    print("No")
