S = input()
ans = ""
for s in S[::-1]:
    if s == ".":
        break
    else:
        ans += s
print(ans[::-1])
