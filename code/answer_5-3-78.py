S = input()
if S[0] == "<" and S.count("<") == 1 and S[-1] == ">" and S.count(">") == 1:
    print("Yes")
else:
    print("No")
