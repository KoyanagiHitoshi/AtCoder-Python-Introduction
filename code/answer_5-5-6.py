N = int(input())
L = list(map(int, input().split()))
print("Yes" if sum(L) > 2*max(L) else "No")
