N, X = map(int, input().split())
S = input()
for i in range(N):
    if S[i] == "o":
        X = X+1
    elif S[i] == "x" and X != 0:
        X = X-1
print(X)
