N = int(input())
S = input()
for i in range(N-1):
    if S[i] != S[i+1]:
        continue
    else:
        print("No")
        break
else:
    print("Yes")
