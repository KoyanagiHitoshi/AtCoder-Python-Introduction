N = int(input())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    if A < B:
        ans += 1
print(ans)
