N, c1, c2 = input().split()
N = int(N)
S = input()
ans = ""
for i in range(N):
    if S[i] != c1:
        ans += c2
    else:
        ans += c1
print(ans)
