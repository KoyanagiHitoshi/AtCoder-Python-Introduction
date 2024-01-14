N, S, K = map(int, input().split())
total = 0
for i in range(N):
    P, Q = map(int, input().split())
    total += P*Q
if total >= S:
    print(total)
else:
    print(total+K)
