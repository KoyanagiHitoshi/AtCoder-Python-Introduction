N = int(input())
S = []
A = []
for i in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))
idx = A.index(min(A))
print(*S[idx:]+S[:idx], sep="\n")
