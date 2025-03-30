N = int(input())
A = list(map(int, input().split()))
if A == sorted(set(A)):
    print("Yes")
else:
    print("No")
