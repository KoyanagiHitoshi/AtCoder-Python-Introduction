S = input()
d = sorted(S)
if d[0] != d[1]:
    print(S.index(d[0])+1)
else:
    print(S.index(d[-1])+1)
