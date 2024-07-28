N = int(input())
S = [input() for i in range(N)]
for i in range(N-2):
    if S[i] == "sweet" and S[i+1] == "sweet":
        print("No")
        break
else:
    print("Yes")
