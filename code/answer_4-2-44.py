N, S = map(int, input().split())
T = list(map(int, input().split()))
p = 0
for t in T:
    if t-p > S:
        print("No")
        break
    p = t
else:
    print("Yes")
