A, B, C, D, E = sorted(map(int, input().split()))
if (A == B == C and D == E) or (A == B and C == D == E):
    print("Yes")
else:
    print("No")
