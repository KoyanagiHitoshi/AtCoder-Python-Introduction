N, M = map(int, input().split())
H = list(map(int, input().split()))
count = 0
for i in range(N):
    M -= H[i]
    if M < 0:
        break
    else:
        count += 1
print(count)
