N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    print(A[i]*A[i+1], end=" ")
