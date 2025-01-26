S = input()
for i in range(1, 16, 2):
    if S[i] == "0":
        continue
    else:
        print("No")
        break
else:
    print("Yes")
