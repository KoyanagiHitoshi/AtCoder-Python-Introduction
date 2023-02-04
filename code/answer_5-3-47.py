H, W = map(int, input().split())
S = [input() for i in range(H)]
ans = 0
for s in S:
    ans += s.count("#")
print(ans)
