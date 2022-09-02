S = input()
c = list(set(S))
print("Yes" if len(c) == 2 and S.count(c[0]) == S.count(c[1]) == 2 else "No")
