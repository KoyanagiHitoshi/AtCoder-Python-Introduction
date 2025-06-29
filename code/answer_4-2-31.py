N = int(input())
A = list(map(int, input().split()))
for i in range(N-2):
    if A[i] == A[i+1] == A[i+2]:
        print("Yes")
        break
else:
    print("No")
