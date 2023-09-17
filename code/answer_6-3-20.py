N = int(input())
P = list(map(int, input().split()))
x = 0
for i in range(1, N):
    x = max(x, P[i])
if P[0] > x:
    print(0)
else:
    print(x-P[0]+1)
