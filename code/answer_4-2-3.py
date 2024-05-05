A = list(map(int, input().split()))
total = 0
for a in A:
    total += a
if total >= 22:
    print("bust")
else:
    print("win")
