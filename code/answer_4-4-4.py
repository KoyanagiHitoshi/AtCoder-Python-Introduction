N = int(input())
A = list(map(int, input().split()))
total = 0
for i in range(N):
    total = total+A[i]
print(total)
