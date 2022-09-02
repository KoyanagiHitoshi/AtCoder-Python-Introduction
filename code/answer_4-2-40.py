A, B = map(int, input().split())
S = input()
print("Yes" if S[A] == "-" and S.count("-") == 1 else "No")
