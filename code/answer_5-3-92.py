S = input()
idx = 1
for s in S:
    if s.isupper():
        break
    else:
        idx += 1
print(idx)
