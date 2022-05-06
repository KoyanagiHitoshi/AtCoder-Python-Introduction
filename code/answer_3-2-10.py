N = int(input())
A = list(map(int, input().split()))
total = 0
for a in A:
    if a > 10:
        total = total+(a-10)
print(total)
