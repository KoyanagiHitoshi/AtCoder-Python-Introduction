A, B, C, D, E = sorted(map(int, input().split()))
print("Yes" if A == B == C and D == E or A == B and C == D == E else "No")
