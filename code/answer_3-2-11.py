N = int(input())
H = list(map(int, input().split()))
ans = 0
for h in H:
    if h > ans:
        ans = h
    else:
        break
print(ans)
