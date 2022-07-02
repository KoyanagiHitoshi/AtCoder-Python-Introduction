A, B, K = map(int, input().split())
ans = 0
while A < B:
    A = A*K
    ans = ans+1
print(ans)
