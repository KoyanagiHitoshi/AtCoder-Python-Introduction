N = int(input())
total = 0
for i in range(1, N+1):
    if (i % 3) != 0 and (i % 5) != 0:
        total = total+i
print(total)
