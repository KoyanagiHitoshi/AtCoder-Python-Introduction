H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 4
if C == 1:
    ans = ans-1
if C == W:
    ans = ans-1
if R == 1:
    ans = ans-1
if R == H:
    ans = ans-1
print(ans)
