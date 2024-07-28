S = list(map(int, input().split()))
flag = True
for i in range(7):
    if S[i] <= S[i+1]:
        continue
    else:
        flag = False
for s in S:
    if 100 <= s <= 675 and s % 25 == 0:
        continue
    else:
        flag = False
print("Yes" if flag else "No")
