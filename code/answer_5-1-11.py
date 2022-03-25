N = int(input())
A = list(map(int, input().split()))
print("Yes" if len(set(A)) == N else "No")
