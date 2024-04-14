S = input()
c = list(set(S))
if len(c) == 2 and S.count(c[0]) == S.count(c[1]) == 2:
    print("Yes")
else:
    print("No")
