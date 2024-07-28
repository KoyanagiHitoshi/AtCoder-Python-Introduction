A = int(input())
ans = 0
for x in range(1, A+1):
    y = A-x
    ans = max(ans, x*y)
print(ans)
