S = input()
flag = True
if S[0] != "<" or S[-1] != ">":
    flag = False
for i in range(1, len(S)-1):
    if S[i] != "=":
        flag = False
if flag:
    print("Yes")
else:
    print("No")
