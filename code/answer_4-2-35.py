N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    if A[i] < A[i+1]:
        continue
    else:
        print("No")
        break
else:
    print("Yes")
