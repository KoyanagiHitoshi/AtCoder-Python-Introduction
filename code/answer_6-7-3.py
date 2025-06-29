S = input()
ans = ""
for s in S:
    if ord("A") <= ord(s) <= ord("Z"):
        ans += s
print(ans)
