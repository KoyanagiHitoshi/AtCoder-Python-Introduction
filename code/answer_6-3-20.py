N = int(input())
t, v = 0, 0
for _ in range(N):
    T, V = map(int, input().split())
    t, v = T, max(0, v-(T-t))+V
print(v)
