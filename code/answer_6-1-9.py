S = [input() for _ in range(12)]
count = 0
for i in range(12):
    if len(S[i]) == i+1:
        count += 1
print(count)
